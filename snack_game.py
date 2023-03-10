#Author: Johnny Phan
#11 grade

import turtle
import random
import time
delay = 0.1
score = 0
high_score = 0


segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score:0   High Score:0", align = "center",font=("Courier",24,"normal"))

def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction =="down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction =="left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction =="right":
        x = head.xcor()
        head.setx(x+20)
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"





wn = turtle.Screen()
wn.title("snake game")
wn.bgcolor("green")
wn.setup(width=600 , height=600)
wn.tracer(0)

#snakehead
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.speed()
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,100)
#food2
food2 = turtle.Turtle()
food2.speed()
food2.shape("circle")
food2.color("blue")
food2.penup()
food2.goto(0,100)


#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")



#Main game loop
while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()
        # reset score
        score = 0
        pen.clear()
        pen.write("score:{}  High Score:{}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        delay = 0.1

    if head.distance(food2) <20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food2.goto(x, y)
        add_segment()
        delay -=.005




    if head.distance(food) < 20:





        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay -= .001

        score+=10

        if score> high_score:
            high_score =score
        pen.clear()
        pen.write("score:{}  High Score:{}".format(score, high_score),align="center",font=("Courier",24,"normal"))

    #move end segments
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

        #move segment 0
    if len(segments) > 0:
        x=head.xcor()
        y= head.ycor()
        segments[0].goto(x, y)

    move()

    #collision with body
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("score:{}  High Score:{}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))
            delay = .1

    time.sleep(delay)

wn.mainloop()

