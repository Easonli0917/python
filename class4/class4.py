# 練習:判斷成績等第
s = int(input("請輸入你的成績:"))
if s >= 90:
    print("你的等第是A")
elif s >= 80:
    print("你的等第是B")
elif s >= 70:
    print("你的等第是C")
elif s >= 60:
    print("你的等第是D")
else:
    print("你的等第是E")
# 練習:判斷奇偶數偶數
m = int(input("請輸入一個數字:"))
if m % 2 == 0:
    print(f"{m}是偶數")
else:
    print(f"{m}是奇數")
# 認識模組
# 匯入模組
import turtle  # 匯入turtle模組

turtle.forward(100)  # 前進100步
turtle.right(90)  # 右轉90度
turtle.done()  # 讓視窗不要關閉
# 好用的
import turtle as t  # 匯入turtle模組並取別名為t

t.forward(100)  # 前進100步
t.right(90)  # 右轉90度
t.done()  # 讓視窗不要關閉
# 練習:使用turtle畫正方形
import turtle as t

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.done()
# for迴圈
# for的組成有三個部分
# for 迴圈變數in範圍
# 迴圈變數只能活在for迴圈裡
# 迴圈變數每回合都會從範圍中取出一個值
for i in range(5):  # range會產生0~4的數字
    print(i)
for i in range(1, 6):  # range會產生1~5的數字
    print(i)
for i in range(1, 6, 2):  # range = 1,3,5
    print(i)
import turtle as t

t.color("blue")
t.shape("turtle")
for i in range(4):
    t.forward(100)
    t.stamp()
    t.right(90)
t.done()
# 蓋印章
import turtle as t

t.color("red")
t.shape("turtle")
for i in range(120):
    t.forward(20)
    t.stamp()
    t.right(8)
t.done()
