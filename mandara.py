import turtle, random
t=turtle.Pen()
turtle.bgcolor('black')
t.hideturtle()
t.speed(0)
for i in range (0,360):
    r=random.random()
    g=random.random()
    b=random.random()
    t.color(r,g,b)
    t.circle(150)
    t.rt(1)
turtle.mainloop()
