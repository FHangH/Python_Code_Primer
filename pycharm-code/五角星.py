#五角星五个顶角36°，平行向内转向144°
#导入turtle绘图工具
import turtle as t

t.hideturtle()#隐藏turtle
t.pensize(6)#线条粗细
t.speed(6)#作图速度

#第一条边
t.pencolor('red')#线条的颜色设定
t.forward(256)#线条前进的矢量距离
t.right(144)#线条向右转向144°

#第二条边
t.pencolor('blue')
t.forward(256)
t.right(144)

#第三条边
t.pencolor('green')
t.forward(256)
t.right(144)

#第四条边
t.pencolor('pink')
t.forward(256)
t.right(144)

#第五条边
t.pencolor('yellow')
t.forward(256)

#绘图结束后留在窗口
t.done()
