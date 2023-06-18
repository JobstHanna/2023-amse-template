import pandas as pd
import sqlite3

# df1 = CO2 of business flights
# df2 = visiting numbers of museums 

df1 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Bussgeld_2016.csv", delimiter=";")
#df1 = pd.read_csv("https://github.com/JobstHanna/2023-amse-template/blob/51492f946bab4dbd11d8325b9fb87dc0417e336e/project/Bussgeld_2016.csv", delimiter=";", on_bad_lines='skip') #engine="python", quotechar='"', on_bad_lines='skip')
#df2 = pd.read_csv("https://github.com/JobstHanna/2023-amse-template/blob/51492f946bab4dbd11d8325b9fb87dc0417e336e/project/Januar_2018.csv", delimiter=";", engine="python", on_bad_lines='skip') #quotechar='"', on_bad_lines='skip')
#df1 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Bussgeld_2016.csv", delimiter=";")
df2 = pd.read_csv("https://offenedaten-koeln.de/sites/default/files/Januar_2018.csv", delimiter=";")
#df3 = pd.read_csv("https://www.kba.de/DE/Themen/ZentraleRegister/FAER/BT_KAT_OWI/bkat_owi_09_11_2021_richText.rtf;jsessionid=0B5A03B15A9FC5A7DC46AD6438EED305.live11311?__blob=publicationFile&v=3", delimiter=";")

#df1.columns.values[]= 'name'
#df2.columns.values[]= 'name'

sink = sqlite3.connect("data/fine_data.sqlite")


df1.to_sql("fine16", sink, if_exists="replace", index=False)
df2.to_sql("fine18", sink, if_exists="replace", index=False)
#df3.to_sql("fine_information", sink, if_exists="replace", index=False)

#print(df1)
#print(df2)






