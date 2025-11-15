import turtle as t

t.speed(0)
t.shape("turtle")
t.color("green")
t.penup()
for i in range(100):
    for a in range(8):
        t.forward(100)
        t.stamp()
        t.left(180)
        t.forward(100)
        t.left(180)
        t.right(45)
    t.clear()
t.done()
