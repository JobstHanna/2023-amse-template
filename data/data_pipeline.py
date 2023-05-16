import pandas as pd
import sqlite3

# df1 = CO2 of business flights
# df2 = visiting numbers of museums 

df1 = pd.read_csv("https://github.com/JobstHanna/2023-amse-template/blob/ea02bdc0d8dc8f14786b663ad6d145caa9fde8f1/project/Kompensationszahlungen_Fluege.csv", sep=",")
df2 = pd.read_csv("https://github.com/JobstHanna/2023-amse-template/blob/c0e5f2a243bf8338bd57e2e720a4482f503912aa/project/Besucherzahlen%20Museen%202019.csv", sep=",")

print(df1)
print(df2)

#df1.columns.values[]= 'name'
#df2.columns.values[]= 'name'

sink = sqlite3.connect("data/flights.sqlite")


df1.to_sql("flights", sink, if_exists="replace")
df2.to_sql("visitors", sink, if_exists="replace")






