import turtle as t
import time

t.speed(0)  # 設定最快速度
t.pensize(0.000000001)
t.shape("turtle")
t.color("green")

for i in range(100000):
    t.pendown()
    t.forward(100)
    t.left(180)
    t.forward(100)
    t.left(180)
    time.sleep(1)
    t.clear()
    t.right(6)
t.done()
