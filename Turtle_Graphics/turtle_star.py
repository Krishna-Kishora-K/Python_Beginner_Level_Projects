from turtle import *

t1=Turtle()
t1.speed(0)
t1.penup()
t1.goto(-200,0)
t1.pendown()
t1.color('red','yellow')
t1.begin_fill()
while True:
    t1.forward(500)              #we can change the value
    t1.left(170)
    if t1.heading()==0:
        break
t1.end_fill()
t1.screen.mainloop()