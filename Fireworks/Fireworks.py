import turtle
import random 

screen = turtle.Screen()
screen.tracer(False)
screen.bgcolor("#161445")

colors = ["red", "green", "orange", "yellow", "purple", "cyan"]

# Create Pen
pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()
pen.setheading(90)

# Create lines for the fireworks
lines = []
direction = 0


for i in range(15):
  line = turtle.Turtle()
  line.hideturtle()
  line.width(2)
  line.setheading(direction)
  direction = direction + 24
  lines.append(line)

def fireworks(x,y):
  pen.penup()
  pen.goto(x, -300)
  pen.pendown()
  while pen.ycor() < y:
    pen.forward(5)
    screen.update()
  pen.clear()
  boom(x,y)

# Code for the explosion
def boom(x,y):
  # setup the lines
  for line in lines:
    color = random.choice(colors)
    line.color(color)
    line.penup()
    line.goto(x,y)
    line.pendown()
