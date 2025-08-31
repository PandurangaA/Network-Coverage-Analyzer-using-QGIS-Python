
import pandas as pd
import random

# Generate sample home locations (lat, lon near Bangalore)
home_data = []
for i in range(1, 21):  # 20 homes
    lat = 12.90 + random.uniform(-0.05, 0.05)
    lon = 77.60 + random.uniform(-0.05, 0.05)
    home_data.append([i, lat, lon])

homes_df = pd.DataFrame(home_data, columns=["id", "Latitude", "Longitude"])
homes_csv_path = "/mnt/data/homes.csv"
homes_df.to_csv(homes_csv_path, index=False)

# Generate sample fiber line coordinates (just as 2 simple lines)
fiber_data = [
    ["Line1", "77.58,12.92 77.62,12.92"],  # east-west line
    ["Line2", "77.60,12.88 77.60,12.94"],  # north-south line
]

fiber_df = pd.DataFrame(fiber_data, columns=["id", "Coordinates"])
fiber_csv_path = "/mnt/data/fiber_lines.csv"
fiber_df.to_csv(fiber_csv_path, index=False)

homes_csv_path, fiber_csv_path
