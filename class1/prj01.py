# 這個是單行註解
print("Hello World")  # 這是程式碼後面的註解
# print("python is fun") Ctrl + ?
"""
這
是
多
行
註
解
"""
# 基本型態
print(123.456)  # 浮點數 Float, float
print(True)  # 布林值 Boolean, bool
print("Hello World")  # 字串 String, str
print(123)  # 整數 Integer, int
# 變數
# = 的功能是可以把右邊的資料存到左邊的變數
a = 10
b = 20
c = a + b

# 變數
# 變數是存放資料的記憶體空間,每個變數都要有自己的名稱
# 要存什麼資料都可以
# 變數名稱命名的規則:只能用英文字母,數字,底線,且不能以數字開頭
# 把 a 和 b 的值相加後再存到 c
print(c)

# 算術運算子
print(a + b)  # 加法
print(a - b)  # 減法
print(a * b)  # 乘法
print(a / b)  # 小數除法
print(a // b)  # 整數除法
print(a % b)  # 取餘數
print(a**b)  # 指數 (次方)

# 運算子的優先順序
"""
1 括號 ()
2 次方 **
3 + - (正負值)
4 *乘法 /除法// 整數除法%取餘數
5 + 加法-減法
"""
# 字串運算
print("Hello" + "World")  # 字串合併
print("Hello" * 3)  # 字串重複
# print("Hello" + 3)  # 錯誤,字串無法家整數
# 除了字串乘法可以跟數字相乘外,其他運算都不行(不同型態間無法運算)
# 字串跟字串之間只能做加法
