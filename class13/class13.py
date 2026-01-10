# def：用來定義函式（function）
# 可以把常用的程式包起來，之後重複使用


def hello():
    print("Hello, World!")


for i in range(3):
    hello()
# 函式也可以有參數（parameter）
# name 是一個參數，呼叫時可以給不同的值


def hello(name):
    print(f"Hello, {name}!")


hello("Alice")
hello("Bob")
hello("Charlie")

for i in range(10):
    hello(i)


# 有回傳值得函數
# 這個函數會回傳一個值當呼叫這個函數時可以把回傳的值存起來
# 在指令當中只要執行return就會回傳值並結束函數
def add(a, b):
    return a + b


print(add(1, 2))
print(add("hello,", "world"))
sum = add(3, 4)
print(sum)

# 有多個回傳值的函數
# 這個函數會回傳兩個值當呼叫這個函數時可以把回傳的值存起來


def add_sub(a, b):
    return a + b, a - b


sum, sub = add_sub(5, 6)
print(f"sum = {sum}, sub = {sub}")


# 多個return
def add_sub(a, b):
    if a > b:
        return a + b
    else:
        return a - b


print(add_sub(5, 6))
print(add_sub(6, 5))
# 函式參數（預設值）


# message 有預設值 "Hello"
def hello(name, message="Hello"):
    print(f"{message}, {name}!")


# 呼叫函式（使用預設參數）

hello("Alice")
hello("Bob", "Good Morning")
# 使用指定參數（指定參數名稱）

hello(name="Charlie", message="Hi")
hello(message="Good Evening", name="David")
# def 區域變數與全域變數
length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數
    # length = length + 1 # 這行會出錯，
    # 因為在函數內部length是區域變數，不能直接修改全域變數
    print("面積是", area)


calculate_square_area()
# print("長度是", area) # 這行會出錯，因為area是區域變數，只能在函數內部使用

length = 5  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數
    print("面積是", area)


length = 10  # 全域變數
calculate_square_area()  # 面積是 100
# 因為要等到函數被呼叫時才會執行，所以area的值是在函數被呼叫時才會被計算


length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    area = length**2  # length是全域變數, area是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 100
# 這時候指令內部的area是區域變數，不會影響到全域變數的值

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area() -> int:
    area = length**2  # length是全域變數, area是區域變數
    return area


area = calculate_square_area()
print("面積是", area)  # 面積是 25

length = 5  # 全域變數
area = 100  # 全域變數


def calculate_square_area():
    global area  # 使用global，將area變成全域變數，可以在函數內部修改全域變數的值
    area = length**2  # length是全域變數, area是區域變數


calculate_square_area()
print("面積是", area)  # 面積是 25
