import random
from turtle import *
def no_of_turtle():
    count=0
    while True:
        count = input("enter the number of turtle(2-20):")
        if count.isdigit():
            count=int(count)
        else:
            print("plz enter numeric value")
            continue
        if 2 <= count <= 20:
            return count
        else:
            print("invalid entry....plz try again")
tc=no_of_turtle()
print(f"Here is the race of {tc} turtles")
width,height=800,800
color_list=["red", "blue", "green", "yellow", "orange","purple", "pink", "cyan", "magenta", "brown","black", "gray", "violet", "gold", "silver","maroon", "navy", "lime", "turquoise", "indigo"]
s1=Screen()
s1.setup(800,800)
def line():
    tl=Turtle()
    tl.speed(0)
    tl.penup()
    tl.goto(-600,-400)
    tl.pendown()
    tl.forward(1000)
    tl.penup()
    tl.goto(-600, 400)
    tl.pendown()
    tl.forward(1000)
    tl.hideturtle()
x_spacing=800//tc+1
turtle_list=[]
line()
for i in range(1, tc + 1):
    tn = Turtle()
    tn.showturtle()
    tn.shape("turtle")
    tn.color(color_list[i-1])
    tn.penup()
    tn.left(90)
    tn.goto(-500 + (i * x_spacing), -400)
    turtle_list.append(tn)
def race():
    race_end=True
    while race_end:
        for t in turtle_list:
            distance= random.randrange(1, 20)
            t.forward(distance)
            x, y = t.pos()
            if y >= 400:
                print(f"the winner is {t.pencolor()} turtle")
                race_end = False
race()
tn.screen.mainloop()