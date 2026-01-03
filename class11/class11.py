# index:尋找定元素在List中第一次出現的位置
# 如果元素不存在則產生錯誤,所以使用前建議檢查元素是否存在
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L.index(5))  # 5

# count:尋找定元素在List中出現的次數
# 這個方法很適合用來檢查重複資料的數量
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L.count(5))  # 1

# sort:將List排序
# 可以指定排序的次序
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L.sort()  # 升序
print(L)
L.sort(reverse=True)  # 降序
print(L)

# reverse:將List反轉
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L.reverse()
print(L)

# List和字串有很多相似之處
# 　我們可以像操作字串一樣來操作List

# 合併兩個list使用+運算子將兩個list連在一起
# 這會產生一個全新的list原本的list不會改變
L1 = [1, 2, 3, 4, 5]
L2 = [6, 7, 8, 9, 10]
L3 = L1 + L2
print(L3)

# 重複list中的內容:*運逤仔讓list的內容重複多次
# 這會產生一個全新的list原本的list不會改變
L1 = [1, 2, 3, 4, 5]
L2 = L1 * 3
print(L2)

# 將字串轉成 List
print(list("Hello"))  # 將字串轉成 List
print(list(range(10)))  # 產生 List
print(list("Hello"))  # 字串轉成 List（範例）

# split 將字串分割成 List
# 依照指定的字元切開字串

s = "Hello World"
l = s.split(" ")  # 以空白分割字串
print(l)

calendar = "2023/12/25"
t = calendar.split("/")  # 以 / 分割字串
print(t)

# join 將 List 轉成字串
# 使用指定字元將 List 串起來

l = ["Hello", "World"]
s = "-".join(l)  # 使用 - 將 List 串成字串
print(s)

print(int())

# 範例：使用 Dictionary (字典)
# 建立 Dictionary，使用 key:value 的配對 (或稱為 map)
# 字典的 key 必需是不可變 (immutable) 的物件 (例如: int, str, tuple)
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d)

# 如果要依據 key 取得 value
# 如果 key 不存在會發生 KeyError
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d["蘋果"])
# print(d["葡萄"])  # 會產生 KeyError, '葡萄' 不存在

# 使用 get 可以避免因為 key 不存在而發生錯誤
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d.get("葡萄"))
print(d.get("葡萄", 0))

# 列出一個字典的所有 key 值
for k in d:
    print(k)  # 這是 Key 值
    print(d[k])  # 以 key 取得對應的 value

# 方式二: 使用 keys() 方法取得所有的 key
for k in d.keys():
    print(k)  # 這是 Key 值
    print(d[k])  # 以 key 取得對應的 value

# 方式三: 使用 values() 方法取得所有的 value
for v in d.values():
    print(v)  # 這是 value

# 方式四: 使用 items() 方法同時取得 key 及 value
for k, v in d.items():
    print(f"{k}: {v}")  # 同時取得 key 與 value，並格式化輸出
