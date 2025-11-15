import turtle as t

t.speed(-100)  # 設定最快速度
t.pensize(10000000000000000000)
t.shape("turtle")
t.color("green")
t.left(90)
t.forward(10000)
t.left(90)
for i inrange(10000000):
    t.forward(100000000)
    t.left(180)
t.done()