# 猜數字遊戲
# 匯入 random 模組並取別名為 r
import random as r

# 隨機生成 1 到 100 之間的一個數字
n = int(r.randint(1, 100))
# 初始化猜測變數為 -1（不可能的值）
a = -1
# while 迴圈，當猜測不等於目標數字時持續執行
while a != n:
    # 要求使用者輸入猜測的數字
    a = int(input("請輸入0 ~ 100 的數字"))
    # 如果猜測的數字比目標數字大
    if a > n:
        print("在小一點")
    # 如果猜測的數字比目標數字小
    elif a < n:
        print("在大一點")
    # 如果猜測正確
    elif a == n:
        print("你猜對了")
