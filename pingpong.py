import turtle
from time import sleep

#creating playfield
#and setting it's parameters
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("#FFEFDB")
screen.setup(width=800, height=600)

screen.tracer(0, 0)
screen.delay(10)


#Score

score_a = 0
score_b = 0


#Panel Left(a)
panel_a = turtle.Turtle()
panel_a.speed(0)
panel_a.shape("square")
panel_a.color("#0000FF")
panel_a.shapesize(stretch_wid=5, stretch_len=1)
panel_a.penup()
panel_a.goto(-350, 0)

#Panel Right(b)
panel_b = turtle.Turtle()
panel_b.speed(0)
panel_b.shape("square")
panel_b.color("#0000FF")
panel_b.shapesize(stretch_wid=5, stretch_len=1)
panel_b.penup()
panel_b.goto(350, 0)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#0000FF")
ball.penup()
ball.goto(0, 0)
#ball movement set (moving ball by set amount in n pix)
ball.dx = 3
ball.dy = 3


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("#0000FF")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24, "normal"))



#Movement and score functions

def panel_a_up():
    y = panel_a.ycor()
    if y < 250:
        y += 20
        panel_a.sety(y)

def panel_a_down():
    y = panel_a.ycor()
    if y > - 250:
        y -= 20
        panel_a.sety(y)

def panel_b_up():
    y = panel_b.ycor()
    if y < 250:
        y += 20
        panel_b.sety(y)

def panel_b_down():
    y = panel_b.ycor()
    if y > -250:
        y -= 20
        panel_b.sety(y)

def scorea():

    turtle.write("Player A won!", align="center", font=("Courier", 30, "normal"))
    turtle.hideturtle()


def scoreb():

    turtle.write("Player B won!", align="center", font=("Courier", 30, "normal"))
    turtle.hideturtle()

#keyboard binding

screen.listen()
screen.onkeypress(panel_a_up, "w")
screen.onkeypress(panel_a_down, "s")
screen.onkeypress(panel_b_up, "Up")
screen.onkeypress(panel_b_down, "Down")


#loop forever
while True:
    sleep(0.001)

    screen.update()
    panel_a.color("#0000FF")
    panel_b.color("#0000FF")

    turtle.clear()



    #move ball across playfield
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bouncing from window game boundaries

    if ball.xcor() > 340 and ball.xcor() < 350 and (
            ball.ycor() < panel_b.ycor() + 40 and ball.ycor() > panel_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        #increases ball speed with every bounce into panel
        ball.dx *= 1.2
        ball.dy *= 1.2

    if ball.xcor() < -340 and ball.xcor() > -350 and (
            ball.ycor() < panel_a.ycor() + 40 and ball.ycor() > panel_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        # increases ball speed with every bounce into panel
        ball.dx *= 1.2
        ball.dy *= 1.2

    #borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        panel_b.color("orange")
        turtle.hideturtle()


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        panel_a.color("orange")
        turtle.hideturtle()


    if score_a == 3:
        # delays display of function
        turtle.ontimer(scorea(), 1000)
        # reset score
        score_a = 0
        score_b = 0
        # reset ball speed to initial
        ball.dx = 3
        ball.dy = 3
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if score_b == 3:
        #delays display of function
        turtle.ontimer(scoreb(), 1000)
        #reset score
        score_a = 0
        score_b = 0
        #reset ball speed to initial
        ball.dx = 3
        ball.dy = 3
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    continue