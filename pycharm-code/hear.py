import turtle as t


def curvemove():

    for i in range(200):
        t.right(1)
        t.forward(1)


t.hideturtle()
t.speed(10)
t.color('red', 'red')
t.begin_fill()
t.left(140)
t.forward(111.65)
curvemove()
t.left(120)
curvemove()
t.forward(111.65)
t.end_fill()
t.done()
