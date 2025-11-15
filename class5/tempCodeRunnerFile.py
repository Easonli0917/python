import turtle as t
import time

t.speed(0)  # 設定最快速度
t.pensize(0.000000001)
t.shape("turtle")
t.color("green")

for i in range(100000):
    for a in range(12):
        t.penup()
        t.forward(150)
        t.stamp()
        t.left(180)
        t.forward(150)
        t.left(180)
        t.left(30 * a)