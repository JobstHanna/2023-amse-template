import pandas as pd
from sqlalchemy import create_engine, types

#ssl._create_default_https_context = ssl._create_unverified_context
sql_types = {
    'EVA_NR': types.BIGINT,
    'DS100': types.TEXT,
    'IFOPT': types.TEXT,
    'NAME': types.TEXT,
    'Verkehr': types.TEXT,
    'Laenge': types.FLOAT,
    'Breite': types.FLOAT,
    'Betreiber_Name': types.TEXT,
    'Betreiber_Nr': types.BIGINT}

df = pd.read_csv("https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV", sep=";")

df = df.drop(columns=["Status"])

valid = ["FV", "RV", "nur DPN"]
df = df[df["Verkehr"].isin(valid)]

df["Laenge"] = df["Laenge"].replace(to_replace=r",", value=".",regex=True).astype(float)
df["Breite"] = df["Breite"].replace(to_replace=r",", value=".",regex=True).astype(float)
df = df(df["Laenge"] >= -90)
df = df(df["Laenge"] <= 90)
df = df(df["Breite"] >= -90)
df = df(df["Breite"] <= 90)

df["IFOPT"] = df["IFOPT"].str.extract('(^[a-zA-Z]{2}:[0-9]*:[0-9]*[:[0-9]*]*)')

# empty cells
df = df.dropna()

engine = create_engine("sqlite:///trainstops.sqlite")
df.to_sql('trainstops',engine ,  if_exists='replace',index= False, dtype= sql_types)

#First, drop the "Status" column
#Then, drop all rows with invalid values:
#Valid "Verkehr" values are "FV", "RV", "nur DPN"
#Valid "Laenge", "Breite" values are geographic coordinate system values between -90 and 90
#Valid "IFOPT" values follow this pattern:
#<exactly two characters>:<any amount of numbers>:<any amount of numbers><optionally another colon followed by any amount of numbers>
#Empty cells are considered invalid
#Use fitting SQLite types (e.g., BIGINT, TEXT or FLOAT) for all columns
