import pandas as pd
import sqlite3

# df1 = CO2 of business flights
# df2 = visiting numbers of museums 

df1 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Bussgeld_2016.csv", delimiter=";")
df2 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/März_2018.csv", delimiter=";")


#df1.columns.values[]= 'name'
#df2.columns.values[]= 'name'

sink = sqlite3.connect("data/flights.sqlite")


df1.to_sql("fine16", sink, if_exists="replace")
df2.to_sql("fine18", sink, if_exists="replace")

#print(df1)
#print(df2)






