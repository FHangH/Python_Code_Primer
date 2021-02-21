#author:fang hao & time:2019/2/24

import turtle as t

t.setup(width=0.6, height=0.6)
t.setup(width=800, height=800, startx=100, starty=100)
t.hideturtle()
t.pensize(6)
t.speed(6)
t.penup()
t.goto(-200, 0)
t.pendown()
t.fillcolor('red')

t.begin_fill()
for _ in range(5):
    t.pencolor('red')
    t.forward(200)
    t.right(144)
t.end_fill()

t.penup()
t.goto(-180, 180)
t.color("blue")
t.write("送你一个五角星，棒棒哒！",font=("Arial",26,"normal"))

t.done()
