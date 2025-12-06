import random

# random 模組的隨機數生成方法
# random.randrange(n) 生成 0 到 n-1 之間的隨機整數
print(random.randrange(10))
# random.randrange(a, b) 生成 a 到 b-1 之間的隨機整數
print(random.randrange(1, 10))
# random.randrange(a, b, step) 生成 a 到 b-1 之間，間隔為 step 的隨機整數
print(random.randrange(1, 10, 2))

# random.randint(a, b) 生成 a 到 b 之間的隨機整數（包括 b）
print(random.randint(1, 10))

# list（列表）介紹
# 列表是一種可以儲存多個資料的資料型態，可以儲存不同型態的資料

# 建立包含整數的列表
l = [1, 2, 3, 4, 5]
print(l)
# 列表可以混合不同型態的資料
l = [1, 2, "Hello World", 4, 5]
print(l)

# list 取值方式
# list 取值跟字串一樣，用[ ]取單個元素或[:] 取多個元素
# list 中的編號（index）都是從 0 開始
l = [1, 2, 3, 4, 5]
print(l[0])  # 取第一個元素
print(l[1])  # 取第二個元素
print(l[2])  # 取第三個元素

# 使用切片語法 [:] 取多個元素
l = [1, 2, 3, 4, 5]
print(l[0:2])  # 取第一個到第二個元素
print(l[2:5])  # 取第三個到第五個元素
print(l[2:])  # 取第三個到最後的元素
print(l[:2])  # 取第一個到第二個元素
print(l[:])  # 取所有元素

# len() 函式可以取得列表的長度
list = [1, 2, 3, 4, 5]
print(len(l))

# 使用 for 迴圈搭配 range 和 len 來逐一取出列表中的每個元素
for i in range(len(list)):
    print(list[i])

# 使用 for 迴圈直接逐一取出列表中的每個元素（更簡潔的方式）
for i in l:
    print(i)
