import turtle as t, random

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def play():
    t.forward(10)
    te.setheading(te.towards(t.pos()))
    te.forward(10)
    if t.distance(ts)<12:
        ts.goto(random.randint(-230, 230), random.randint(-230, 230))
    if t.distance(te)<12:
        Playing=False
        score=0
    if Playing:
        t.ontimer(play,100)

t.shape("turtle")
t.speed(0)
t.color('black')
t.penup()

te=t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.penup()
te.goto(0,200)

ts=t.Turtle()
ts.shape('circle')
ts.color('orange')
ts.speed(0)
ts.penup()
ts.goto(0,-200)

t.onkeypress(turn_right, " Right ")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()

t.mainloop()
