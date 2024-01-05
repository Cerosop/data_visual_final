import json
from flask import Flask, jsonify, request, render_template, redirect
import sqlite3 as lite
app = Flask(__name__)

@app.route('/')
def redir():
    return redirect('/main')


@app.route('/main', methods=['GET', 'POST'])
def page1():
    con = lite.connect('mydb.db')
    if request.method == 'POST':
        cate = request.values['cate'].split(", ")
        with con:
            cur=con.cursor()
            
            print(cate)
            res = []
            
            if cate[1] == 'people' or cate[1] == 'money ave':
                cur.execute(f"select {cate[0]}, count(*) as count from data where year = \'{cate[2]}\' group by {cate[0]}")
                con.commit()
                people = cur.fetchall()
                people = sorted(people, key=lambda x: x[0], reverse=False)
                
                if cate[0] == 'work':
                
                else:
                    b = 0
                    if cate[0] == 'age':
                        b = 5
                    if cate[0] == 'money':
                        b = 5 
                    res1 = []
                    i = 0
                    for a in people:
                        if i * b > a[0]:
                            res1[i] += a[1]
                        if i * b <= a[0]:
                            while i * b <= a[0]:
                                i += 1
                            res1[i] = a[1]
                    people = []
                    for i, a in enumerate(res1):
                        people.append((i - 1, a))
            
            if cate[1] == 'money' or cate[1] == 'money ave':
                cur.execute(f"select {cate[0]}, sum(money) as sum from data where year = \'{cate[2]}\' group by {cate[0]}")
                con.commit()
                money = cur.fetchall()
                money = sorted(money, key=lambda x: x[0], reverse=False)
                
                if cate[0] == 'work':
                
                else:
                    b = 0
                    if cate[0] == 'age':
                        b = 5
                    if cate[0] == 'money':
                        b = 5
                    res1 = []
                    i = 0
                    for a in money:
                        if i * b > a[0]:
                            res1[i] += a[1]
                        if i * b <= a[0]:
                            while i * b <= a[0]:
                                i += 1
                            res1[i] = a[1]
                    money = []
                    for i, a in enumerate(res1):
                        money.append((i - 1, a))
                        
                        
            if cate[1] == 'money':
                res = money
            if cate[1] == 'people':
                res = people
            if cate[1] == 'money ave':
                for i, a in enumerate(money):
                    res.append((a[0], a[1] / people[i][1]))
              
            # res = sorted(res, key=lambda x: x[0], reverse=False)
            print(res)  
            data = {'res': '-1', 'data': res}
            return jsonify(data)
    else:    
        return render_template('main.html')


if __name__ == '__main__':
    app.debug = True
    app.run()