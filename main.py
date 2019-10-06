from turtle import *
import random
import threading
from tkinter import *

# generate random seed
num = random.randint(1897348294, 18495729473285739)
print("\n\nUsing Seed: " + str(num))
# set the seed for all randomization
random.seed(num)
# save the current seed to a text file
with open('current_seed.txt', 'w') as f:
    f.write(str(num))

# colors
colors = ['blue', 'red', 'purple', 'yellow', 'green', 'orange', 'hot_colors']
# create the turtle
turtle1 = Turtle()
# make it so there is no arrow drawing the lines
turtle1.ht()
# get window size
screen = Screen()
# set the background color
screen.bgcolor('white')
# set the screen size
screen.screensize(canvwidth=512, canvheight=512)
# get the screen height and width
w = screen.window_width()
h = screen.window_height()
# printing just for reference
print(screen.screensize())
# enable the following line to have a more precise image
# w, h = w // 2, h // 2

# set the turtle speed
turtle1.speed(0)  # max speed is 0


def chooseColor():
    """
    chooses random color then opens that color's respective shade text file.
    then it randomly chooses a shade for the previous chosen color.
    """
    color = random.choice(colors)
    with open("colors/" + color + '.txt', 'r') as f:
        shades = f.read().splitlines()
    rgb = random.choice(shades)
    print("Using " + color + " with rgb " + rgb)
    return rgb


def draw_background(a_turtle):
    """ Draw a background rectangle. """
    ts = a_turtle.getscreen()
    canvas = ts.getcanvas()
    height = ts.getcanvas()._canvas.winfo_height()
    width = ts.getcanvas()._canvas.winfo_width()

    turtleheading = turtle1.heading()
    turtlespeed = turtle1.speed()
    penposn = turtle1.position()
    penstate = turtle1.pen()

    turtle1.penup()
    turtle1.speed(0)  # fastest
    turtle1.goto(-width / 2 - 2, -height / 2 + 3)
    turtle1.fillcolor(Screen().bgcolor())
    turtle1.begin_fill()
    turtle1.setheading(0)
    turtle1.forward(width)
    turtle1.setheading(90)
    turtle1.forward(height)
    turtle1.setheading(180)
    turtle1.forward(width)
    turtle1.setheading(270)
    turtle1.forward(height)
    turtle1.end_fill()

    turtle1.penup()
    turtle1.setposition(*penposn)
    turtle1.pen(penstate)
    turtle1.setheading(turtleheading)
    turtle1.speed(turtlespeed)


draw_background(turtle1)


def square():
    """
        Draws square with angles of 70 to 91 degrees, with
        side lengths of 100 to 201

        Guess you can't call it a square anymore
    """
    m = random.randint(70, 91)
    d = random.randint(100, 201)
    for i in range(4):
        rgb = chooseColor()
        turtle1.pencolor(rgb)
        turtle1.right(m)
        turtle1.forward(d)


def hexagon():
    """
        Draws hexagon with angles of 70 to 91 degrees, with
        side lengths of 100 to 201

        Guess you can't call it a hexagon anymore
    """
    m = random.randint(70, 91)
    d = random.randint(100, 201)
    turtle1.right(90)
    for i in range(4):
        rgb = chooseColor()
        turtle1.pencolor(rgb)
        turtle1.forward(m)
        turtle1.right(d)
    turtle1.forward(d)


def triangle():
    """
        Draws triangle with angles of 70 to 91 degrees, with
        side lengths of 100 to 201

        Guess you can't call it a triangle anymore
    """
    m = random.randint(70, 91)
    d = random.randint(100, 201)

    for i in range(3):
        rgb = chooseColor()
        turtle1.pencolor(rgb)
        turtle1.forward(m)
        turtle1.right(-d)


# set variables for counting
j = 0
m = 50

while True:
    x, y = turtle1.pos()  # Get x, y positions.
    if abs(x) > w or abs(y) > h:  # Check if pen is outside of frame
        # reset pen to random position on X and Y between 0 and the frame border
        theX = random.randint(0, w - 100)
        theY = random.randint(0, h - 100)
        turtle1.setx(theX)
        turtle1.sety(theY)
    # draw a triangle, a hexagon and a square
    triangle()
    hexagon()
    square()
    j += 1
    # if program has run the above 50 times, its time for another save
    if j == m:
        print("\n\nSAVING!!!!!!!!!\n\n")
        # get the current screen
        ts = turtle1.getscreen()
        # save the drawing to a post script
        ts.getcanvas().postscript(file="fun.eps")
        m += 50
