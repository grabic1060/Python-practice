import turtle as T
import random
T.colormode(255)
T.hideturtle()
T.shape('circle')
T.bgcolor('black')
T.color('yellow')
T.speed(0)
for i in range(0,50):
    T.circle(150)
    T.lt(360/50)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    T.color(r,g,b)
T.exitonclick()

