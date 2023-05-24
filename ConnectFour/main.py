import turtle
import time

window = turtle.Screen()
window.setup(400,400)
window.setworldcoordinates(-500,-500,500,500)
window.title("Connect 4")
turtle.speed(0)
turtle.hideturtle()
window.tracer(0,0)

score = turtle.Turtle()
score.up()
score.hideturtle()

ROWS = 6
COLS = 7 
STARTX = -450 
STARTY = -450*ROWS/COLS
WIDTH = -2*STARTX
HEIGHT = -2*STARTY

def drawRectangle(x,y,w,h,color):
  turtle.up()
  turtle.goto(x,y)
  turtle.seth(0)
  turtle.down()
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.fd(w)
  turtle.left(90)
  turtle.fd(h)
  turtle.left(90)
  turtle.fd(w)
  turtle.left(90)
  turtle.fd(h)
  turtle.left(90)
  turtle.end_fill()

def drawCircle(x,y,r,color):
  turtle.up()
  turtle.goto(x, y - r)
  turtle.seth(0)
  turtle.down()
  turtle.fillcolor(color)
  turtle.begin_fill()
  turtle.circle(r, 360, 150)
  turtle.end_fill()
  
  
  
  
