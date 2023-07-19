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