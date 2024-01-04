import json
from flask import Flask, jsonify, request, render_template, redirect
import sqlite3 as lite
app = Flask(__name__)

@app.route('/')
def redir():
    return redirect('/page1')

@app.route('/main', methods=['GET', 'POST'])
def page1():
    con = lite.connect('mydb.db')
    if request.method == 'POST':
        x = request.values['x']
        y = request.values['y']
        print(x, y)
        with con:
            cur=con.cursor()
            cur.execute(f"select {x}, count(*) as count from data group by {x}")
            con.commit()
            res = cur.fetchall()
            print(res)
            res = dict(res)
            
            print(res)
            data = {'res': '-1', 'data': res}
            return jsonify(data)
    else:    
        return render_template('main.html')


if __name__ == '__main__':
    app.debug = True
    app.run()