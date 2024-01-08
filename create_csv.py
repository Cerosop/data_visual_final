import sqlite3 as lite
import pandas as pd
con = lite.connect('mydb.db')
limit = 20
res = {}

selected_columns = ['date', 'name', 'category', 'value']
dict = [{'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}, 
        {'date': [], 'name': [], 'category': [], 'value': []}]

with con:
    cur=con.cursor()
    
    for y in range(2011, 2023):
        if y == 2013 or y == 2019:
            continue
        
        cur.execute(f"select name, money, continent from data where year = {y} limit {limit}")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[0]['date'].append(str(y) + "-01-01")
            dict[0]['name'].append(d[0])
            dict[0]['category'].append(d[2])
            dict[0]['value'].append(d[1])
        
        cur.execute(f"select work from data where year = {y}")
        con.commit()
        data = cur.fetchall()
        d = {}
        for a in data:
            l = a[0].split(", ")
            for s in l:
                if d.get(s):
                    d[s] += 1
                else:
                    d[s] = 1
        for k in d:
            dict[1]['date'].append(str(y) + "-01-01")
            dict[1]['name'].append(k)
            dict[1]['category'].append(k)
            dict[1]['value'].append(d[k])
            
        cur.execute(f"select work, money from data where year = {y}")
        con.commit()
        data = cur.fetchall()
        d = {}
        for a in data:
            l = a[0].split(", ")
            for s in l:
                if d.get(s):
                    d[s] += a[1]
                else:
                    d[s] = a[1]
        data = []
        for k in d:
            dict[2]['date'].append(str(y) + "-01-01")
            dict[2]['name'].append(k)
            dict[2]['category'].append(k)
            dict[2]['value'].append(d[k])
            
        cur.execute(f"select continent, count(*) as count from data where year = {y} group by continent")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[3]['date'].append(str(y) + "-01-01")
            dict[3]['name'].append(d[0])
            dict[3]['category'].append(d[0])
            dict[3]['value'].append(d[1])
            
        cur.execute(f"select continent, sum(money) as count from data where year = {y} group by continent")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[4]['date'].append(str(y) + "-01-01")
            dict[4]['name'].append(d[0])
            dict[4]['category'].append(d[0])
            dict[4]['value'].append(d[1])
            
        cur.execute(f"select country, count(*) as count from data where year = {y} and continent = 'Asia' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[5]['date'].append(str(y) + "-01-01")
            dict[5]['name'].append(d[0])
            dict[5]['category'].append(d[0])
            dict[5]['value'].append(d[1])
            
        cur.execute(f"select country, sum(money) as count from data where year = {y} and continent = 'Asia' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[6]['date'].append(str(y) + "-01-01")
            dict[6]['name'].append(d[0])
            dict[6]['category'].append(d[0])
            dict[6]['value'].append(d[1])
            
        cur.execute(f"select country, count(*) as count from data where year = {y} and continent = 'North America' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[7]['date'].append(str(y) + "-01-01")
            dict[7]['name'].append(d[0])
            dict[7]['category'].append(d[0])
            dict[7]['value'].append(d[1])
            
        cur.execute(f"select country, sum(money) as count from data where year = {y} and continent = 'North America' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[8]['date'].append(str(y) + "-01-01")
            dict[8]['name'].append(d[0])
            dict[8]['category'].append(d[0])
            dict[8]['value'].append(d[1])
            
        cur.execute(f"select country, count(*) as count from data where year = {y} and continent = 'South America' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[9]['date'].append(str(y) + "-01-01")
            dict[9]['name'].append(d[0])
            dict[9]['category'].append(d[0])
            dict[9]['value'].append(d[1])
            
        cur.execute(f"select country, sum(money) as count from data where year = {y} and continent = 'South America' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[10]['date'].append(str(y) + "-01-01")
            dict[10]['name'].append(d[0])
            dict[10]['category'].append(d[0])
            dict[10]['value'].append(d[1])
            
        cur.execute(f"select country, count(*) as count from data where year = {y} and continent = 'Europe' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[11]['date'].append(str(y) + "-01-01")
            dict[11]['name'].append(d[0])
            dict[11]['category'].append(d[0])
            dict[11]['value'].append(d[1])
            
        cur.execute(f"select country, sum(money) as count from data where year = {y} and continent = 'Europe' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[12]['date'].append(str(y) + "-01-01")
            dict[12]['name'].append(d[0])
            dict[12]['category'].append(d[0])
            dict[12]['value'].append(d[1])
            
        cur.execute(f"select country, count(*) as count from data where year = {y} and continent = 'Oceania' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[13]['date'].append(str(y) + "-01-01")
            dict[13]['name'].append(d[0])
            dict[13]['category'].append(d[0])
            dict[13]['value'].append(d[1])
            
        cur.execute(f"select country, sum(money) as count from data where year = {y} and continent = 'Oceania' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[14]['date'].append(str(y) + "-01-01")
            dict[14]['name'].append(d[0])
            dict[14]['category'].append(d[0])
            dict[14]['value'].append(d[1])
            
        cur.execute(f"select country, count(*) as count from data where year = {y} and continent = 'Africa' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[15]['date'].append(str(y) + "-01-01")
            dict[15]['name'].append(d[0])
            dict[15]['category'].append(d[0])
            dict[15]['value'].append(d[1])
            
        cur.execute(f"select country, sum(money) as count from data where year = {y} and continent = 'Africa' group by country")
        con.commit()
        data = cur.fetchall()
        for d in data:
            dict[16]['date'].append(str(y) + "-01-01")
            dict[16]['name'].append(d[0])
            dict[16]['category'].append(d[0])
            dict[16]['value'].append(d[1])
            

df = pd.DataFrame(dict[0])
with open('static/js/files/name_m.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[1])
with open('static/js/files/work_c.csv', 'w', newline='', encoding='utf-8') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[2])
with open('static/js/files/work_m.csv', 'w', newline='', encoding='utf-8') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[3])
with open('static/js/files/continent_c.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[4])
with open('static/js/files/continent_m.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[5])
with open('static/js/files/Asia_c.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[6])
with open('static/js/files/Asia_m.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[7])
with open('static/js/files/North America_c.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[8])
with open('static/js/files/North America_m.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[9])
with open('static/js/files/South America_c.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[10])
with open('static/js/files/South America_m.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[11])
with open('static/js/files/Europe_c.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[12])
with open('static/js/files/Europe_m.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[13])
with open('static/js/files/Oceania_c.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[14])
with open('static/js/files/Oceania_m.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[15])
with open('static/js/files/Africa_c.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)
df = pd.DataFrame(dict[16])
with open('static/js/files/Africa_m.csv', 'w', newline='') as file:
    df.to_csv(file, index=False)