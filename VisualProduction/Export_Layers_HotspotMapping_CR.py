import arcpy, os, timeit

start = timeit.default_timer()

aprx = arcpy.mp.ArcGISProject("CURRENT")
m = aprx.listMaps("Costa Rica")[0]
docPath = r"C:\Users\olive\Box Sync\Hotspot Stoplight Resources\Maps\Working\CostaRica"


lyt = aprx.listLayouts("CostaRica")[0]

print('water'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

lyrList = m.listLayers("WorldWaterBodies")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"Water.PNG", transparent_background=True, resolution=300)


print('roads'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("OSM")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"Roads.PNG", transparent_background=True, resolution=300)


print('mask'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("Mask_CostaRica")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"Mask.PNG", transparent_background=True, resolution=300)


print('WDPA_Graduated'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("WDPA_Graduated")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"WDPA_Graduated.PNG", transparent_background=True, resolution=300)


print('UrbanMask'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("Anthromes_10m_UrbanMask")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"UrbanMask.PNG", transparent_background=True, resolution=300)


print('remnant habitat'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("Anthromes_Reclass_10m")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"RemnantHabitat.PNG", transparent_background=True, resolution=300)


print('population density'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("POPULATION")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"PopDensity.PNG", transparent_background=True, resolution=300)


print('urban expansion'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("1km Urban Expansion")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"UrbanExpansion_2050.PNG", transparent_background=True, resolution=300)


print('IUCN Threatened Species'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("IUCN_Species_CR.tif")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"IUCN_Threatened_Species.PNG", transparent_background=True, resolution=300)



print('MSA_2050'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("TerrestrialMSA_2050_SSP3_RCP6_Clip")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"MSA_2050_SSP3_RCP6.PNG", transparent_background=True, resolution=300)



print('MSA_2015'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("TerrestrialMSA_2030_World_Clip")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"MSA_2015.PNG", transparent_background=True, resolution=300)



print('MSA_Change'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("MSA_Loss_2050_SSP3RCP6")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"MSA_Change_2050_SSP3_RCP6.PNG", transparent_background=True, resolution=300)


print('Biodiversity Intactness'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("BiodiversityIntactness_2020.tif")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"Biodiversity_Intactness_2020.PNG", transparent_background=True, resolution=300)


print('LC_Vulnerability'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("Land_Cover_Vulnerability_2050_Mask")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"Land_Cover_Vulnerability_2050.PNG", transparent_background=True, resolution=300)


print('RiverFloodRisk'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("rf.tif_intensity")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"RiverFloodRisk.PNG", transparent_background=True, resolution=300)


print('UrbanHeatExtremes'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("Landsat9_Thermal_Extremes_SanJose.tif")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"ThermalExtremes.PNG", transparent_background=True, resolution=300)

##_________________________________________________________________________________________________________________


lyt = aprx.listLayouts("CostaRica_10x")[0]


print('Hillshade'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("Terrain: Multi-Directional Hillshade")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"Hillshade.PNG", transparent_background=True, resolution=30)


print('Aerial'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("World Imagery")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"Aerial.PNG", transparent_background=True, resolution=30)


print('Ocean'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

for lyr in lyrList:   
   lyr.visible = False

lyrList = m.listLayers("World Ocean Base")
for lyr in lyrList:   
   lyr.visible = True

lyt.exportToPNG(docPath+"\\"+"Ocean.PNG", transparent_background=True, resolution=30)


for lyr in lyrList:   
   lyr.visible = False

stop = timeit.default_timer()

total_time = (stop - start)
print(total_time)