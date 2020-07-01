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

#paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(+350, 0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=5, stretch_len=1)
ball.penup()
ball.goto(0, 0)

#main game loop
while True:
    wn.update()
