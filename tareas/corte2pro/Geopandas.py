import geopandas as gpd

localidades_shp = gpd.read_file(r"C:\Users\jasser villarreal\Desktop\corte2pro\taller_loca.shp")
localidades_shp
#()
print(localidades_shp.head(5))