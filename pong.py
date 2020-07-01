
# Simple pong game in python 3 

#imports turtle module
import turtle

#created window
wn = turtle.Screen()

#titles window
wn.title ("Pong by Bloodshot TRD")

#sets background color
wn.bgcolor("black")

#window size parameters
wn.setup(width=800, height=600)

#stops window from updating
wn.tracer(0)

#paddle 1 parameters
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

#paddle 2 parameters
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(+350, 0)


#ball parameters
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
#sets ball to move by 2 pixels on x and y coordinates
ball.dx = .25
ball.dy = .25


#functions for animation
def paddle_1_up():
    #returns paddle coordinate
    y = paddle_1.ycor()
   #adds 20 position to y coordinate
    y += 20
    #sets paddle to new coordinate
    paddle_1.sety(y)

def paddle_1_down():
    #returns paddle coordinate
    y = paddle_1.ycor()
   #adds 20 position to y coordinate
    y -= 20
    #sets paddle to new coordinate
    paddle_1.sety(y)

def paddle_2_up():
    #returns paddle coordinate
    y = paddle_2.ycor()
   #adds 20 position to y coordinate
    y += 20
    #sets paddle to new coordinate
    paddle_2.sety(y)

def paddle_2_down():
    #returns paddle coordinate
    y = paddle_2.ycor()
   #adds 20 position to y coordinate
    y -= 20
    #sets paddle to new coordinate
    paddle_2.sety(y)

#keyboard binding up to wkeypress
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")


#main game loop
while True:
    wn.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1