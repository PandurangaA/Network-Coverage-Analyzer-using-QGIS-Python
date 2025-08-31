import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString

# Load CSV (id, Coordinates like "77.58,12.92 77.62,12.92")
fiber_df = pd.read_csv("C:\\Users\\pandu\\OneDrive\\Desktop\\Real Project\\QGIS with python\\Network Coverage Analyzer\\homes.shp")

line_geoms = []
for coords in fiber_df["Coordinates"]:
    points = [tuple(map(float, c.split(","))) for c in coords.split()]
    line_geoms.append(LineString(points))

fiber_gdf = gpd.GeoDataFrame(fiber_df, geometry=line_geoms, crs="EPSG:4326")

# Save as shapefile
fiber_gdf.to_file("fiber_lines.shp", driver="ESRI Shapefile")
print("✅ Fiber shapefile created: fiber_lines.shp")
