import json
import math
from flask import Flask, jsonify, request, render_template, redirect
import sqlite3 as lite
app = Flask(__name__)

@app.route('/')
def redir():
    return redirect('/home')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
    

@app.route('/page1', methods=['GET', 'POST'])
def page1():
    con = lite.connect('mydb.db')
    if request.method == 'POST':
        cate = request.get_json()['cate'].split(", ")
        print(cate)
        with con:
            cur=con.cursor()
            cur.execute(f"select * from data where year = \'{cate[1]}\' order by {cate[0]} {cate[2]}")
            con.commit()
            res = cur.fetchall()
            
            if cate[0] == 'age' and cate[2] == 'asc':
                cur.execute(f"select * from data where year = \'{cate[1]}\' and age = -1 order by name {cate[2]}")
                con.commit()
                res2 = cur.fetchall()
                res = [a for a in res if a[3] != -1]
                res += res2
                
            res = [[i + 1, d[1], d[3], d[4], d[5], d[6], d[7]] for i, d in enumerate(res)]
            
            for i in range(1, len(res)):
                if (cate[0] == 'money' and res[i][6] == res[i - 1][6]) or (cate[0] == 'age' and res[i][2] == res[i - 1][2]):
                    res[i][0] = res[i - 1][0]
            
            print(res)  
            data = {'data': res}
            return jsonify(data)
    else:    
        with con:
            cur=con.cursor()
            cur.execute(f"select * from data where year = 2022 order by money desc")
            con.commit()
            res = cur.fetchall()
            res = [[i + 1, d[1], d[3], d[4], d[5], d[6], d[7]] for i, d in enumerate(res)]
            
            for i in range(1, len(res)):
                if res[i][6] == res[i - 1][6]:
                    res[i][0] = res[i - 1][0]
            
            print(json.dumps(res))  
            return render_template('page1.html', res = json.dumps(res))
        
        
@app.route('/page2', methods=['GET', 'POST'])
def page2():
    con = lite.connect('mydb.db')
    limit = 20
    res = {}
    res['continent'] = {}
    res['continent']['people'] = {}
    res['continent']['money'] = {}
    res['work'] = {}
    res['work']['people'] = {}
    res['work']['money'] = {}
    res['age'] = {}
    res['age']['people'] = {}
    res['age']['money'] = {}
    
    with con:
        cur=con.cursor()
        
        for y in range(2011, 2023):
            cur.execute(f"select continent, count(*) as count from data where year = {y} group by continent")
            con.commit()
            data = cur.fetchall()
            data = sorted(data, key=lambda x: x[1], reverse=True)
            res['continent']['people'][y] = data
            
            cur.execute(f"select continent, sum(money) as count from data where year = {y} group by continent")
            con.commit()
            data = cur.fetchall()
            data = sorted(data, key=lambda x: x[1], reverse=True)
            res['continent']['money'][y] = data
            
            
            cur.execute(f"select work, count(*) as count from data where year = {y} group by work")
            con.commit()
            data = cur.fetchall()
            data = sorted(data, key=lambda x: x[0], reverse=False)
            data = preuse('work', data)
            data = sorted(data, key=lambda x: x[1], reverse=True)
            other = ('other', sum(d[1] for d in data[limit - 1:]))
            data = data[:limit - 1]
            data.append(other)
            res['work']['people'][y] = data
        
            cur.execute(f"select work, sum(money) as count from data where year = {y} group by work")
            con.commit()
            data = cur.fetchall()
            data = sorted(data, key=lambda x: x[0], reverse=False)
            data = preuse('work', data)
            data = sorted(data, key=lambda x: x[1], reverse=True)
            other = ('other', sum(d[1] for d in data[limit - 1:]))
            data = data[:limit - 1]
            data.append(other)
            res['work']['money'][y] = data
            
            
            cur.execute(f"select age, count(*) as count from data where year = {y} group by age")
            con.commit()
            data = cur.fetchall()
            data = sorted(data, key=lambda x: x[0], reverse=False)
            data = preuse('age', data)
            data = sorted(data, key=lambda x: x[1], reverse=True)
            res['age']['people'][y] = data
        
            cur.execute(f"select age, sum(money) as count from data where year = {y} group by age")
            con.commit()
            data = cur.fetchall()
            data = sorted(data, key=lambda x: x[0], reverse=False)
            data = preuse('age', data)
            data = sorted(data, key=lambda x: x[1], reverse=True)
            res['age']['money'][y] = data
     
    print(res)
    return render_template('page2.html', res = json.dumps(res))


@app.route('/page3', methods=['GET', 'POST'])
def page3():
    con = lite.connect('mydb.db')
    if request.method == 'POST':
        cate = request.get_json()['cate'].split(", ")
        print(cate)
        with con:
            cur=con.cursor()
            
            if cate[1] == 'people' or cate[1] == 'money ave':
                cur.execute(f"select {cate[0]}, count(*) as count from data where year = \'{cate[2]}\' group by {cate[0]}")
                con.commit()
                people = cur.fetchall()
                people = sorted(people, key=lambda x: x[0], reverse=False)
                
                people = preuse(cate[0], people)
            
            if cate[1] == 'money' or cate[1] == 'money ave':
                cur.execute(f"select {cate[0]}, sum(money) as sum from data where year = \'{cate[2]}\' group by {cate[0]}")
                con.commit()
                money = cur.fetchall()
                money = sorted(money, key=lambda x: x[0], reverse=False)
                
                money = preuse(cate[0], money)
            
            res = []  
            if cate[1] == 'money':
                res = money
            if cate[1] == 'people':
                res = people
            if cate[1] == 'money ave':
                for i, a in enumerate(money):
                    if people[i][1]:
                        res.append((a[0], a[1] / people[i][1]))
                    else:
                        res.append((a[0], 0))
            
            print(res)  
            data = {'data': res}
            return jsonify(data)
    else:    
        with con:
            cur=con.cursor()
            cur.execute(f"select age, count(*) as count from data where year = 2022 group by age")
            con.commit()
            people = cur.fetchall()
            people = sorted(people, key=lambda x: x[0], reverse=False)
            people = preuse('age', people)
            
            res = people
            print(res)  
            return render_template('page3.html', res = json.dumps(res))


def preuse(cate, data_list):
    if cate == 'work': # work要拆開
        limit = 20
        d = {}
        for a in data_list:
            l = a[0].split(", ")
            for s in l:
                if d.get(s):
                    d[s] += a[1]
                else:
                    d[s] = a[1]

        d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        data_list = []
        i = 0
        c = 0
        for k in d:
            i += 1
            if i <= limit:
                data_list.append((k, d[k]))
            else:
                break
                # c += d[k]
        data_list = (sorted(data_list, key=lambda x: x[0], reverse=False))
        # data_list.append(('other', c))
    elif cate == 'age' or cate == 'money': # age, money要用range 前者表示range a * b ~ (a + 1) * b - 1
        b = 0
        if cate == 'age':
            b = 5
            res1 = [0 for i in range(int(150/b))]
        if cate == 'money':
            b = 5 
            res1 = [0 for i in range(int(250/b))]
            
        
        i = 0
        for a in data_list:
            while i * b <= a[0]:
                i += 1
            res1[i] += a[1]
            
        data_list = []
        x = False
        for i, a in enumerate(res1):
            if not i:
                data_list.append((i - 1, a))
            if a and i:
                x = True
            if x:
                data_list.append((i - 1, a))
        for i in range(len(data_list) - 1, -1, -1):
            if data_list[i][1]:
                break
            data_list.pop(i)
                
    return data_list
    
    
@app.route('/page4', methods=['GET', 'POST'])
def page4():
    # return render_template('pytest/run.html')
    return render_template('page4.html')


@app.route('/page5', methods=['GET', 'POST'])
def page5():
    con = lite.connect('mydb.db')
    with con:
        cur=con.cursor()
        cur.execute(f"select money, age, count(*) from data where year = 2022 group by money, age ")
        con.commit()
        m_a = cur.fetchall()
        m_a = [a for a in m_a if a[1] != -1]
        
        cur.execute(f"select year, money, count(*) from data group by year, money ")
        con.commit()
        y_m = cur.fetchall()
        value_y_m = [a[2] for a in y_m]
        
        mean_value = sum(value_y_m) / len(value_y_m)
        std_dev = math.sqrt(sum((x - mean_value) ** 2 for x in value_y_m) / len(value_y_m))

        # 对列表进行标准化
        value_y_m = [(x - mean_value) / std_dev for x in value_y_m]
        lowest = min(value_y_m)
        y_m = [[y_m[i][0], y_m[i][1], value_y_m[i] - lowest] for i in range(len(y_m))]
        print(y_m)
        print()
        
        cur.execute(f"select year, age, count(*) from data group by year, age ")
        con.commit()
        y_a = cur.fetchall()
        y_a = [a for a in y_a if a[1] != -1]
        value_y_a = [a[2] for a in y_a]
        
        mean_value = sum(value_y_a) / len(value_y_a)
        std_dev = math.sqrt(sum((x - mean_value) ** 2 for x in value_y_a) / len(value_y_a))

        # 对列表进行标准化
        value_y_a = [(x - mean_value) / std_dev for x in value_y_a]
        lowest = min(value_y_a)
        y_a = [[y_a[i][0], y_a[i][1], value_y_a[i] - lowest] for i in range(len(y_a))]
        print(y_a)
        
        cur.execute(f"select money, age, year, count(*) from data group by money, age, year ")
        con.commit()
        m_a_y = cur.fetchall()
        m_a_y = [a for a in m_a_y if a[1] != -1]
        
        res = [m_a, y_m, y_a, m_a_y]
        
        # for a in res:
        #     print(a)
        #     print()
        # print(res)  
        return render_template('page5.html', res = json.dumps(res))


@app.route('/page6', methods=['GET', 'POST'])
def page6():
    con = lite.connect('mydb.db')
    if request.method == 'POST':
        age = request.get_json()['age']
        continent = request.get_json()['continent']
        print(age, continent)
        with con:
            cur=con.cursor()
            cur.execute(f"select count(*) from data where year = 2022 and age < {(age // 5 + 1) * 5} and age >= {age // 5 * 5}")
            con.commit()
            age_count = cur.fetchall()[0][0]
            
            if age_count:
                cur.execute(f"select name, money from data where year = 2022 and age < {(age // 5 + 1) * 5} and age >= {age // 5 * 5} limit 1")
                con.commit()
                age_max = cur.fetchall()[0]
            else:
                age_max = ("no one", 0)
            
            cur.execute(f"select count(*) from data where year = 2022 and continent = \'{continent}\'")
            con.commit()
            con_count = cur.fetchall()[0][0]
            
            if con_count:
                cur.execute(f"select name, money from data where year = 2022 and continent = \'{continent}\' limit 1")
                con.commit()
                con_max = cur.fetchall()[0]
                
                cur.execute(f"select work, money from data where year = 2022 and continent = \'{continent}\'")
                con.commit()
                con_work = cur.fetchall()
                con_work = max(preuse('work', con_work), key=lambda x: x[1])
            else:
                con_max = ("no one", 0)
                con_work = con_max
            
            
            
            res = [age_count, age_max, con_count, con_max, con_work]
            
            print(res)  
            data = {'data': res}
            return jsonify(data)
    else:     
        return render_template('page6.html')
    
    
if __name__ == '__main__':
    app.debug = True
    app.run()
