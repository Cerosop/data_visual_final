import pandas as pd
import sqlite3

conn = sqlite3.connect('mydb.db')
cur = conn.cursor()

cur.execute(f"DELETE FROM data")
conn.commit()

df = pd.read_csv("forbes_billionaires_list.csv")

for i, d in df.iterrows():
    name = str(d['name'])
    name = name.replace('\'', '`')
    
    source = str(d['source'])
    source = source.replace("\'", '`')
    
    year = int(d['year'])
    
    age = -1
    if pd.notna(d['age']):
        age = int(d['age'])
        
    money = int(d['net_worth'])
    
    
    cur.execute(f'insert into data (name, year, age, country, continent, work, money) values(\'{name}\', {year}, {age}, \'{d["citizenship"]}\', \'{d["continents"]}\', \'{source}\', {money})')
    conn.commit()
    
conn.close()
