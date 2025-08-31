# Network-Coverage-Analyzer-using-QGIS-Python

Overview

This project demonstrates how Python (PyQGIS) and QGIS can be combined to analyze fiber network coverage and optimize pole placement for broadband expansion.
It solves a real-world problem in the networking domain by automating serviceability checks, identifying uncovered homes, and suggesting cost-efficient rollout strategies.
----------------------------------------------------------
Features

✅ Import home locations (points) and fiber lines (polylines) into QGIS

✅ Automated buffer analysis around fiber lines (service radius)

✅ Identify covered vs. uncovered homes within the buffer

✅ Suggest optimal pole placements at fixed intervals near high-demand areas

✅ Export final results as shapefiles & coverage maps for visualization
---------------------------------------------------------------------
Tech Stack

QGIS 3.x (Open-source GIS platform)

PyQGIS (Python inside QGIS for automation)

GeoPandas / Shapely (for geospatial operations, optional)

Matplotlib / QGIS Print Composer (for map visualization)



Project Structure
Network-Coverage-Analyzer/
│── data/
│   ├── homes.csv
│   ├── fiber_lines.csv
│── scripts/
│   ├── coverage_analysis.py
│   ├── pole_placement.py
│── outputs/
│   ├── coverage_map.png
│   ├── homes_coverage.shp
│   ├── poles.shp
│── README.md

















--------------------------------------------
How It Works (Steps)

Load Data: Import homes (.csv) and fiber lines (.csv or .shp) into QGIS.

Run Script: Execute Python script (coverage_analysis.py) from the QGIS Python Console.

Buffer Creation: Script creates coverage zones around fiber lines (e.g., 300m).

Home Classification: Homes inside buffer = covered, outside buffer = uncovered.

Pole Placement: Suggests pole positions at regular intervals where uncovered homes exist.

Export Results: Save outputs as shapefiles and coverage maps for planning reports.

-------------------------------------------------------
Example Output

Coverage Map (Sample)
(Add a screenshot here — from QGIS showing fiber lines, covered homes in green, uncovered homes in red, poles in blue)
---------------------------------------------------------
Installation & Usage

1] Install QGIS 3.x → Download QGIS

2] Clone this repo: git clone https://github.com/yourusername/network-coverage-analyzer.git
cd network-coverage-analyzer

3] Open QGIS → Load homes.csv and fiber_lines.csv.

4] Open QGIS Python Console → Run scripts/coverage_analysis.py.

5] View results in the Layers Panel and export shapefiles/maps.

Real-World Impact

1] Reduced manual coverage analysis time by 60–70%

2] Improved accuracy of serviceability checks

3]  Helped in cost-optimized network rollout planning

Future Enhancements

1] Add machine learning for predicting high-demand areas

2] Integrate with PostGIS / SQL for scalable data storage

3] Build a simple web dashboard for visualization


