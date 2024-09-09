#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.ny.gov", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.ny.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("39hk-dx4f", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# Access longitude and latitude for a specific station (e.g., the first station)
station_1_longitude = results_df['gtfs_longitude'].iloc[0]
station_1_latitude = results_df['gtfs_latitude'].iloc[0]

print(f"Longitude: {station_1_longitude}, Latitude: {station_1_latitude}")