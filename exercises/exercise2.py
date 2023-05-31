import pandas as pd

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

airports = pd.read_csv("ttps://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV", sep=";")

airports.to_sql('trainstops', 'sqlite:///trainstops.sqlite', if_exists='replace', index=False)

#First, drop the "Status" column
#Then, drop all rows with invalid values:
#Valid "Verkehr" values are "FV", "RV", "nur DPN"
#Valid "Laenge", "Breite" values are geographic coordinate system values between -90 and 90
#Valid "IFOPT" values follow this pattern:
#<exactly two characters>:<any amount of numbers>:<any amount of numbers><optionally another colon followed by any amount of numbers>
#Empty cells are considered invalid
#Use fitting SQLite types (e.g., BIGINT, TEXT or FLOAT) for all columns
