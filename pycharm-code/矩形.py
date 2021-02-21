#导入turtle
import turtle as t
t.hideturtle()#隐藏turtle
t.pensize(6)#线条粗细
t.speed(6)#作图速度

#第一条边
t.pencolor('blue')#线条颜色
t.forward(256)#前进256，系统默认向右前进
t.right(90)#右转90°

#第二条边
t.pencolor('green')
t.forward(256)
t.right(90)

#第三条边
t.pencolor('pink')
t.forward(256)
t.right(90)

#第四条边
t.pencolor('yellow')
t.forward(256)#此时正方形已经画出，无需转向

t.done()#结束后停留在窗口


