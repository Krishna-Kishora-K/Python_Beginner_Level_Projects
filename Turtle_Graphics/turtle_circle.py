import turtle
from turtle import *
import random

t1=Turtle()
turtle.colormode(255)
t1.speed(0)
while True:
    t1.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    t1.circle(200)
    t1.left(5)
    if t1.heading()==0:
        break
t1.screen.mainloop()