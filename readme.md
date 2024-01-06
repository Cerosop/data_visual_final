### 記得要時常pull，push也是，不然會車禍，車禍就把你剛剛改的地方先複製然後刪掉，先pull下來再改

#### 看資料格式的方法:
執行maini.py <br>
http://127.0.0.1:5000/main 在main.html第22行有2個東西，分別是age or money和年份，按下按鈕後console有資料，放了那個年份的人由年齡或資產排序<br>
http://127.0.0.1:5000/run 放了每一年按照資產排的人名。然後在run.html第34行有3個東西，分別代表x, y, 條件，按下按鈕後console有資料(x可以是name, work, country, continent，y可以是people, money，條件就洲的名稱或all或no)<br>
http://127.0.0.1:5000/graph 在graph.html第22行有3個東西，分別代表x, y, 年，按下按鈕後console有資料(x可以是age, money, work, country, continent，y可以是people, money, money ave)<br>
http://127.0.0.1:5000/circle 給圓餅圖用的，看了就知道<br>
http://127.0.0.1:5000/map 放了2022年前100有錢的人的名字和國家<br>

可以去看'參考'裡面的東西，特別是templates裡test4_1.html與test4_3.html跟main.py的互動關係，我有在那兩個html打註解寫你們可以看的地方，那些是html獲取後端資料的2種方法，對應的是py裡的
```python
return render_template('test4_1.html', outs = res)
```
和
```python
data = {'res': '2'}
return jsonify(data)
```

你們的html寫在外層的templates裡


