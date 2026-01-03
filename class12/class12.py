# 字典 / Dictionary（用 key 找 value）

# 建立字典
d = {"蘋果": 20, "香蕉": 30, "櫻桃": 25}

# 讀取資料（用 key 找 value）
print(d["蘋果"])

# 修改資料
d["蘋果"] = 10  # 修改「蘋果」對應的 value
print(d)

# 新增一組 key-value
d["橘子"] = 15
print(d)
# 刪除字典中的資料

d = {"蘋果": 20, "香蕉": 30, "櫻桃": 25}

# 用 pop 刪除（用 key）
d.pop("香蕉")

# 如果 key 不存在，會出現 KeyError
# d.pop("西瓜")

popitem = d.pop("蘋果")
print(d)
print(popitem)

# len：查看字典裡有幾組 key-value

d = {"蘋果": 20, "香蕉": 30, "櫻桃": 25}
print(len(d))

# pop 刪除字典資料
# 如果 key 不存在，會出現 KeyError（程式會出錯）

popitem = d.pop("香蕉")  # 不存在會錯誤
print(d)  # {'蘋果': 20, '櫻桃': 25}
print(popitem)  # 被刪除的資料

# len：取得字典中有多少組 key-value 資料

d = {"蘋果": 20, "香蕉": 30, "櫻桃": 25}
print(len(d))

# in：檢查 key 是否存在字典中
# 只檢查 key，不是 value

d = {"蘋果": 20, "香蕉": 30, "櫻桃": 25}

print("蘋果" in d)  # True，因為 key 存在
print("西瓜" in d)  # False，因為 key 不存在

# 檢查 key 是否存在於字典中
# 可以避免發生 KeyError 錯誤

d = {"蘋果": 20, "香蕉": 30, "櫻桃": 25}

print("蘋果" in d)  # True，因為 key 存在
print("西瓜" in d)  # False，因為 key 不存在

# 檢查數字是否存在於 List 中
# in 也可以用在 List

L = [1, 2, 3, 4, 5]

print(3 in L)  # True，3 在 List 中
