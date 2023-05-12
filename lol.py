import turtle, random
t=turtle.Pen()
t.shape('turtle')
t.penup()
t.speed(0)
while True:
    x=random.randint(-1000,960)
    y=random.randint(-580,540)
    t.write('ㅄ', font=('Arial',24,'bold'))
    t.goto(x,y)
