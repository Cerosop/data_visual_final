from flask import Flask, jsonify, request, render_template, redirect
import sqlite3 as lite
app = Flask(__name__)

@app.route('/')
def redir():
    return redirect('/circle')


@app.route('/main', methods=['GET', 'POST'])
def page1():
    con = lite.connect('./mydb.db')
    if request.method == 'POST':
        cate = request.values['cate'].split(", ")
        print(cate)
        with con:
            cur=con.cursor()
            cur.execute(f"select * from data where year = \'{cate[1]}\' order by \'{cate[0]}\' asc")
            con.commit()
            res = cur.fetchall()
            res = [(i + 1, d[1], d[3], d[4], d[5], d[6], d[7]) for i, d in enumerate(res)]
            
            print(res)  
            data = {'res': '-1', 'data': res}
            return jsonify(data)
    else:    
        return render_template('pytest/main.html')
    
    
@app.route('/run', methods=['GET', 'POST'])
def page2():
    # return render_template('pytest/run.html')
    return render_template('index2.html')


def preuse(cate, data_list):
    if cate == 'work': # work要拆開
        d = {}
        for a in data_list:
            l = a[0].split(", ")
            for s in l:
                if d.get(s):
                    d[s] += a[1]
                else:
                    d[s] = a[1]
        
        data_list = []
        for k in d:
            data_list.append((k, d[k]))
    else: # age, money要用range 前者表示range a * b ~ (a + 1) * b - 1
        b = 0
        if cate == 'age':
            b = 5
        if cate == 'money':
            b = 5 
            
        res1 = [0 for i in range(int(150/b))]
        i = 0
        for a in data_list:
            while i * b <= a[0]:
                i += 1
            res1[i] += a[1]
            
        data_list = []
        for i, a in enumerate(res1):
            if a:
                data_list.append((i - 1, a))
                
    return data_list


@app.route('/graph', methods=['GET', 'POST'])
def page3():
    con = lite.connect('mydb.db')
    if request.method == 'POST':
        cate = request.values['cate'].split(", ")
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
                    res.append((a[0], a[1] / people[i][1]))
            
            print(res)  
            data = {'res': '-1', 'data': res}
            return jsonify(data)
    else:    
        return render_template('pytest/graph.html')
    
    
@app.route('/circle', methods=['GET', 'POST'])
def page4():
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
    return render_template('pytest/circle.html', res = res)


@app.route('/map', methods=['GET', 'POST'])
def page5():
    con = lite.connect('mydb.db')
    limit = 100
    with con:
        cur=con.cursor()
        y = 2022
        cur.execute(f"select name, country from data where year = {y} limit {limit}")
        con.commit()
        data = cur.fetchall()
    
    print(data)
    return render_template('pytest/map.html', res = data)
    
    
if __name__ == '__main__':
    app.debug = True
    app.run()
