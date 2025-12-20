# append 可以在已經存在的List當中加入新的資料
# 可以在程式執行的過程當中可以將資料加入道以存在的List的"最後面"
L = ["hello", "world"]
L.append("python")
print(L)

# insert在程式執行的過程中可以將資料存到列表的指定位置
# 記得List的index是重零開始
# 如果新增的的位置超過List的長度會接加到最後面
# 如果新增的複數會從後面開始算起例如-1是最後一個位置
L = ["hello", "world"]
L.insert(1, "python")
print(L)
L.insert(-1, "java")
print(L)
L.insert(10, "c++")
print(L)

# remove 可以將List當中的指定資料刪除
L = ["hello", "world", "python"]
L.remove("world")
print(L)

# pop: 移除並傳回 List 中的元素
L = ["Hello", "World", "Python"]
# 不寫參數時，pop() 會移除最後一個元素
L.pop()  # 移除並傳回最後一個元素
print(L)  # ["Hello", "World"]

s = L.pop(1)  # 如果索引值存在，可以取得索引值的元素
print(s)  # World
print(L)  # ["Hello"]
# 如果傳入的index範圍錯誤，會產生例外訊息
# 負索引也可以使用
L = ["Hello", "World", "Python"]
L.pop(-2)  # 移除並傳回倒數第二個元素
print(L)  # ["Hello", "Python"]
# 負索引，逆向索引值位置從最後開始數
