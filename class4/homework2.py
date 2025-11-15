import turtle as t

t.speed(-100)  # 設定最快速度
t.pensize(0.000000001)
t.shape("turtle")
t.color("green")
for i in range(1000):
    t.stamp()
    t.forward(i)
    t.right(50)
t.done()
