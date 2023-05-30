import pandas as pd
import sqlite3

# df1 = CO2 of business flights
# df2 = visiting numbers of museums 

df1 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Bussgeld_2016.csv", delimiter=";")
#df1 = pd.read_csv("https://github.com/JobstHanna/2023-amse-template/blob/51492f946bab4dbd11d8325b9fb87dc0417e336e/project/Bussgeld_2016.csv", delimiter=";", on_bad_lines='skip') #engine="python", quotechar='"', on_bad_lines='skip')
#df2 = pd.read_csv("https://github.com/JobstHanna/2023-amse-template/blob/51492f946bab4dbd11d8325b9fb87dc0417e336e/project/Januar_2018.csv", delimiter=";", engine="python", on_bad_lines='skip') #quotechar='"', on_bad_lines='skip')
#df1 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Bussgeld_2016.csv", delimiter=";")
df2 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Januar_2018.csv", delimiter=";")

#df1.columns.values[]= 'name'
#df2.columns.values[]= 'name'

df1.replace(to_replace="", value='a')
df2.replace(to_replace='"', value='a')

sink = sqlite3.connect("data/fine_data.sqlite")


df1.to_sql("fine16", sink, if_exists="replace", index=False)
df2.to_sql("fine18", sink, if_exists="replace", index=False)

#print(df1)
#print(df2)






