from turtle import *
import random
t1=Turtle()
colormode(255)
t1.speed(0)
for i in range(1000):
    t1.pencolor((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    t1.dot(20)
    t1.penup()
    t1.goto(random.randint(-400,400),random.randint(-300,300))
    t1.pendown()
t1.screen.mainloop()