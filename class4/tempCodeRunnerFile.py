import turtle as t

t.shape("turtle")
t.color("green")
t.penup()
for i in range(1000000):
    t.stamp()
    t.forward(20)
    t.right(5 * i)
t.done()
