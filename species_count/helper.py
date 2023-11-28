import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import shapely
import time
from geocube.api.core import make_geocube
# from geocube.rasterize import rasterize_points_griddata, rasterize_points_radial

pd.set_option('display.max_columns', 30)

def to_utm_crs(target_polygon):
    """
    Input: a polygon of the area of interest
    Output: a polygon of the area of interest in utm_crs
    """
    # get the centroid of the target polygon
    centroid = target_polygon.centroid
    # get the utm zone of the centroid
    utm_zone = int(((centroid.x.mean() + 180) // 6) + 1)
    utm_crs = f'EPSG:326{utm_zone}' if centroid.y.mean() > 0 else f'EPSG:327{utm_zone}'
    # convert the target polygon to utm_crs
    gdf = gpd.GeoDataFrame({
        'geometry': [target_polygon]
    }, crs='EPSG:4326')  # EPSG:4326 is the standard CRS for geographic coordinates (WGS 84)
    gdf_meters = gdf.to_crs(utm_crs)
    return gdf_meters['geometry'][0]

def create_grid_pointwise(target_polygon, resolution):
    """
    Input: a polygon of the area of interest; resolution(in meters)
    Output: A list of the grid coordinates of the given resolution.
    """
    lon_per_meter = 0.000008983
    lat_per_meter = 0.000010966
    lon_resolution = resolution * lon_per_meter
    lat_resolution = resolution * lat_per_meter
    x = np.arange(target_polygon.bounds[0],target_polygon.bounds[2],lon_resolution)
    y = np.arange(target_polygon.bounds[1],target_polygon.bounds[3],lat_resolution)
    points = []
    for i in x:
        for j in y:
            p=shapely.geometry.Point(i,j)
            # There are too many points, so we only includes points that are within the target polygon
            if p.within(target_polygon):
                points.append(shapely.geometry.Point(i,j))
    return points

def create_grid(target_polygon, resolution):
    """
    Input: a polygon of the area of interest; resolution(in meters)
    Output: A list of the polygons(in utm_crs) of the given resolution.
    """
    xmin, ymin, xmax, ymax = target_polygon.bounds
    rows = int(np.ceil((ymax-ymin) / resolution))
    cols = int(np.ceil((xmax-xmin) / resolution))
    XleftOrigin = xmin
    XrightOrigin = xmin + resolution
    YtopOrigin = ymax
    YbottomOrigin = ymax- resolution
    polygons = []
    for i in range(cols):
        Ytop = YtopOrigin
        Ybottom =YbottomOrigin
        for j in range(rows):
            polygons.append(shapely.geometry.Polygon([(XleftOrigin, Ytop), (XrightOrigin, Ytop), (XrightOrigin, Ybottom), (XleftOrigin, Ybottom)]))
            Ytop = Ytop - resolution
            Ybottom = Ybottom - resolution
        XleftOrigin = XleftOrigin + resolution
        XrightOrigin = XrightOrigin + resolution
    return polygons

def count_species(species_geo, point_list):
    """
    Input: A gpd series of geometry representing the intersection of each species with the area of interest; A list of the grid coordinates of the given resolution.
    Output: A list of the count of species in each grid.
    """
                
    species_count = []
    for p in point_list:
        species_count.append(sum(species_geo.contains(p)))
    return species_count


def filter_species(path, target_polygon):
    """
    Input: a file path of the species shp file; a polygon of the area of interest
    Output: A gpd series of geometry representing the intersection of each species with the area of interest
    """
    species_df = gpd.read_file(path)
    # filter out species that is extinct(contains 'extinct' in legend)
    species_df = species_df[~species_df['legend'].str.contains('Extinct')]
    # choose only species in CR
    species_df = species_df[species_df.geometry.intersects(target_polygon)]
    # get the intersection area of each species with CR
    species_df['intersection_geometry'] = species_df.geometry.intersection(target_polygon)
    species_geo = species_df.intersection_geometry
    return species_geo

def plot_abundance(count_df, species_name):
    # plot CR map with species count
    fig, ax = plt.subplots(figsize=(20,10))
    # gpd.GeoSeries(cr_polygon).plot(ax=ax, color='white', edgecolor='black')
    # plot costa rica map
    cr_map=gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')).query('name == "Costa Rica"')
    cr_map.plot(ax=ax, color='white', edgecolor='black')
    # use a colormap to plot the species count
    count_df.plot(ax=ax, column='species_count', legend=True, cmap='Greens')
    # set the title
    ax.set_title('{} Abundance in CR'.format(species_name), fontsize=20)


def output_geotiff(input_df,output_path, resolution):
    """
    convert the geo dataframe to geotiff and save it to path
    """
    out_grd = make_geocube(
        vector_data=input_df,
        measurements=["species_count"],
        resolution=(-resolution,resolution),
    )
    out_grd = out_grd.rio.reproject("EPSG:4326")
    out_grd["species_count"].rio.to_raster(output_path)
    return out_grd