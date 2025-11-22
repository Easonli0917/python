import turtle as t
import time

t.speed(0)  # 設定最快速度
t.pensize(2)
t.shape("turtle")
t.color("green")
t.pendown()
for i in range(100000):
    t.forward(100)
    t.back(100)
    time.sleep(1)
    t.clear()
    t.right(6)
t.done()
