import turtle as t

t.shape("turtle")
t.color("green")
t.penup()
for i in range(1000000):
    t.stamp()
    t.forward(i)
    t.right(i + 10)