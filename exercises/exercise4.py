import pandas as pd
import urllib.request
import zipfile
import sqlite3

# down flie
def download_zip(url, file):
    urllib.request.urlretrieve(url, file)


# unzip
def unzip_file(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as csv:
        csv.extractall(extract_path)
        
def store(df, path, tablename):
    conn = sqlite3.connect(path)
    df.to_sql(tablename, conn, index=False, if_exists="replace")
    #   conn.close()
    

def transform(csv):
    # important columns
    columns = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]

    # dataframe 
    df = pd.read_csv(csv, sep=";", decimal=",", usecols=columns, index_col=False)
    
    # rename columns
    df = df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})
    return df


def cel_to_fahr(df):
    # change Celsius to Fahrenheit
    df["Temperatur"] = (df["Temperatur"] * 9 / 5) + 32
    df["Temperatur"] = df["Temperatur"].round(2)

    df["Batterietemperatur"] = (df["Batterietemperatur"] * 9 / 5) + 32
    df["Batterietemperatur"] = df["Batterietemperatur"].round(2)
    return df

def validate(df):
    # Geraet to be an id over 0
    df = df[df["Geraet"] > 0]
    df = df[df["Monat"] > 0]
    return df
    
    
def main():
    zip_file = "mowesta-dataset.zip"
    csv_file = "data.csv"
    db = "temperatures.sqlite"
    
    # download zip
    download_zip("https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip", zip_file)
    
    # unzip file
    unzip_file(zip_file, ".")

    # load data
    df = transform(csv_file)
    
    # change temp unit
    df = cel_to_fahr(df)

    # validate data
    df = validate(df)

    # store data
    store(df, db, "temperatures")



if __name__ == "__main__":
    main()