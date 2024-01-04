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

* 記得要時常pull，務必記得，push也是，不然會車禍 *
