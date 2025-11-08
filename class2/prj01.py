# 字串格式化 f-string
name = "張三"
age = 18
print(f"名字:{name},年齡:{age}")
# 只要在字串前面加F,就可以在字串中使用大括弧
# 任何資料都可以放進去
# 就可以成為一個新字串
# 這種方式稱為f-string

# 函式是由名稱,括號組成
# 括號裡可以放入參數(提供的材料)每一個都要用逗號分隔
# max() 函式,會回傳函式當中最大的值
print(max(1, 2, 3, 4, 5))

# len() 函式,會回傳字串的長度
print(len("Hello World"))

# type() 函式,會回傳資料的型態
print(type(123))
print(type("Hello World"))
print(type(True))
print(type(3.14))

# int() 函式,可以把參數轉換成整數
print(int(3.14))
print(int(True))
print(int("123"))

# float() 函式,可以把參數轉換成浮點數
print(float(True))
print(float(123))
print(float("3.14"))

# bool() 函式,可以把參數轉換成布林值
print(bool(0))
print(bool(123))
print(bool("Hello World"))
print(bool(""))

# str() 函式,可以把參數轉換成字串
print(str(123))
print(str(3.14))
print(str(True))

# input() 函式,可以讓使用者在程式執行的過程中輸入資料
name = input("請輸入名字:")  # 提式的文字會顯示在螢幕上,不會被記錄
print(type(name))  # 回傳字串
print(f"你叫{name}")  # 字串格式化
print("你叫" + name)  # 字串合併
age = int(input("請輸入年齡:"))
print(f"明年你將會{age+1}歲")
