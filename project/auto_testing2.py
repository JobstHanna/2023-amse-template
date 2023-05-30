import pandas as pd
import sqlite3
import urllib.request as ur
from pandas.testing import assert_frame_equal
from numpy import NaN

def extract(url):
    return ur.urlopen(url)

def interpreterCsv(data):
    return pd.read_csv

def tranform(data):
    return data.dropna()

def load(data, db):
    sink = sqlite3.connect(db)
    data.ro_sql('example', sink, if_exists='replace', index=False)
    sink.close()
    
def etl(url, db):
    data = extract(url)
    data = interpreterCsv(data)
    data = transfrom(data)
    load(data, db)
    
def test_transform():
    data= pd.DataFrame([[''], [], []])
    transformed = transfrom(data)
    
    assert transformed.shaped =(2, 3)
    
def test_load():
    data = pd.DataFrame([[''], [], []])
    load(data, 'test.sqlite')
    
    sink = sqlite3.connect('test.sqlite')
    result = pd.read_sql_query("SELECT * FROM example", sink)
    sink.close()
    
    assert_frame_equal(result, data)