

from qgis.core import QgsVectorLayer, QgsProject, QgsGeometry, QgsFeature, QgsSpatialIndex
import csv

# Load home points layer
homes_layer = QgsVectorLayer("path/to/homes.shp", "Homes", "ogr")

# Load fiber lines and create 500m buffer
fiber_layer = QgsVectorLayer("path/to/fiber.shp", "Fiber", "ogr")
buffer_distance = 500  

buffered_fiber = [f.geometry().buffer(buffer_distance, 5) for f in fiber_layer.getFeatures()]

# Spatial index for faster search
home_index = QgsSpatialIndex(homes_layer.getFeatures())

results = []
for home in homes_layer.getFeatures():
    home_geom = home.geometry()
    covered = False
    for bf in buffered_fiber:
        if bf.contains(home_geom):
            covered = True
            break
    results.append([home["id"], home_geom.asPoint().x(), home_geom.asPoint().y(), "Covered" if covered else "Not Covered"])

# Save results to CSV
with open("network_coverage_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Home_ID", "Latitude", "Longitude", "Coverage_Status"])
    writer.writerows(results)

print("✅ Report generated: network_coverage_report.csv")
