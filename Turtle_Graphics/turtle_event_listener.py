from turtle import *
screen=Screen()
t1=Turtle()
def up():
    t1.setheading(90)
    t1.forward(20)
def down():
    t1.setheading(270)
    t1.forward(20)
def right():
    t1.setheading(0)
    t1.forward(20)
def left():
    t1.setheading(180)
    t1.forward(20)
def move():
    t1.forward(30)
def clear_screen():
    t1.clear()
    t1.penup()
    t1.home()
    t1.pendown()
def circle():
    t1.circle(100)
def curvel():
    t1.left(10)
    t1.forward(10)
def curver():
    t1.right(10)
    t1.forward(10)
def curvedl():
    t1.right(10)
    t1.back(10)
def curveur():
    t1.left(10)
    t1.back(10)
screen.listen()
screen.onkey(fun=up,key='u')
screen.onkey(fun=down,key='d')
screen.onkey(fun=right,key='r')
screen.onkey(fun=left,key='l')
screen.onkey(fun=move,key='m')
screen.onkey(fun=clear_screen,key='x')
screen.onkey(fun=circle,key='c')
screen.onkey(fun=curvel,key='Left')
screen.onkey(fun=curver,key='Right')
screen.onkey(fun=curvedl,key='Down')
screen.onkey(fun=curveur,key='Up')
screen.mainloop()