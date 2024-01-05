import json
from flask import Flask, jsonify, request, render_template, redirect
import sqlite3 as lite
app = Flask(__name__)

@app.route('/')
def redir():
    return redirect('/main')


def preuse(cate, data_list):
    if cate[0] == 'work': # work要拆開
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
        if cate[0] == 'age':
            b = 5
        if cate[0] == 'money':
            b = 5 
            
        res1 = [0 for i in range(30)]
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


@app.route('/main', methods=['GET', 'POST'])
def page1():
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
                
                people = preuse(cate, people)
            
            if cate[1] == 'money' or cate[1] == 'money ave':
                cur.execute(f"select {cate[0]}, sum(money) as sum from data where year = \'{cate[2]}\' group by {cate[0]}")
                con.commit()
                money = cur.fetchall()
                money = sorted(money, key=lambda x: x[0], reverse=False)
                
                money = preuse(cate, money)
            
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
        return render_template('main.html')


if __name__ == '__main__':
    app.debug = True
    app.run()