import pandas as pd
import sqlite3

conn = sqlite3.connect('mydb.db')
cur = conn.cursor()

cur.execute(f"DELETE FROM data")
conn.commit()

df = pd.read_csv("forbes_billionaires_list.csv")

for i, d in df.iterrows():
    source = str(d['source'])
    name = str(d['name'])
    source = source.replace("\'", '`')
    name = name.replace('\'', '`')
    
    cur.execute(f'insert into data (name, year, age, country, continent, work, money) values(\'{name}\', \'{d["year"]}\', \'{d["age"]}\', \'{d["citizenship"]}\', \'{d["continents"]}\', \'{source}\', \'{d["net_worth"]}\')')
    conn.commit()
    
conn.close()
