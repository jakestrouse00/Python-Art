from turtle import Turtle, Screen
import turtle
import random
import atexit
from tkinter import *
from PIL import ImageTk, Image
import threading


turtle.tracer(0, 0)

class Colors:
    def __init__(self):
        self.colors = {
            "blue": ["#5dade2", "#1b4f72", "#21618c", "#2874a6", "#2e86c1", "#3498db"],
            "red": ["#78281f", "#943126", "#b03a2e", "#cb4335", "#e74c3c", "#ec7063"],
            "purple": [
                "#6c3483",
                "#5b2c6f",
                "#884ea0",
                "#76448a",
                "#512e5f",
                "#633974",
            ],
            "yellow": [
                "#B7950B",
                "#D4AC0D",
                "#F1C40F",
                "#F4D03F",
                "#F7DC6F",
                "#F9E79F",
            ],
            "green": ["#1D8348", "#239B56", "#28B463", "#2ECC71", "#58D68D", "#82E0AA"],
            "orange": [
                "#EB984E",
                "#F0B27A",
                "#F5CBA7",
                "#CA6F1E",
                "#E67E22",
                "#EB984E",
            ],
        }
        """"hot_colors": [
                "#FF1493",
                "#FF7F50",
                "#7CFC00",
                "#ADFF2F",
                "#7FFF00",
                "#00FFFF",
            ]"""

    def choose_color(self):
        main_color = random.choice(list(self.colors.keys()))
        secondary_color = random.choice(self.colors[main_color])
        return secondary_color


class Pen:
    def __init__(self, w, h):
        self.t1 = Turtle()
        self.w = w
        self.h = h
        self.colors = Colors()
        self.setup()

    def setup(self):
        self.t1.ht()

        self.t1.speed()
        self.t1.pensize(2)

    def forward(self):
        color = self.colors.choose_color()
        self.t1.pencolor(color)
        length = random.randint(10, 100)
        self.t1.forward(length)

    def rotate(self):
        rotation = random.randint(10, 350)
        self.t1.right(rotation)

    def check_pos(self):
        x, y = self.t1.pos()  # Get x, y positions.
        if abs(x) > self.w or abs(y) > self.h:  # Check if pen is outside of frame
            # reset pen to random position on X and Y between 0 and the frame border
            theX = random.randint(0, self.w - 100)
            theY = random.randint(0, self.h - 100)
            self.t1.penup()
            self.t1.setx(theX)
            self.t1.sety(theY)
            self.t1.pendown()

    def draw(self):
        self.check_pos()
        self.rotate()
        self.forward()


def draw_background(a_turtle):
    """ Draw a background rectangle. """
    ts = a_turtle.getscreen()
    canvas = ts.getcanvas()
    height = ts.getcanvas()._canvas.winfo_height()
    width = ts.getcanvas()._canvas.winfo_width()

    turtleheading = a_turtle.heading()
    turtlespeed = a_turtle.speed()
    penposn = a_turtle.position()
    penstate = a_turtle.pen()

    a_turtle.penup()
    a_turtle.speed(0)  # fastest
    a_turtle.goto(-width / 2 - 2, -height / 2 + 3)
    a_turtle.fillcolor(Screen().bgcolor())
    a_turtle.begin_fill()
    a_turtle.setheading(0)
    a_turtle.forward(width)
    a_turtle.setheading(90)
    a_turtle.forward(height)
    a_turtle.setheading(180)
    a_turtle.forward(width)
    a_turtle.setheading(270)
    a_turtle.forward(height)
    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.setposition(*penposn)
    a_turtle.pen(penstate)
    a_turtle.setheading(turtleheading)
    a_turtle.speed(turtlespeed)


class Drawer:
    def __init__(self, amount: int):

        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.screensize(canvwidth=512, canvheight=512)
        self.w = self.screen.window_width()
        self.h = self.screen.window_height()

        t = Turtle()
        draw_background(t)

        atexit.register(self.save)
        self.pointers = [Pen(self.w, self.h) for _ in range(amount)]

    def save(self):
        print("SAVING!!!!!!!!!")
        # get the current screen
        ts = self.pointers[0].t1.getscreen()
        # save the drawing to a post script
        ts.getcanvas().postscript(file="art_save.eps")

    def start(self):
        while True:
            for i in self.pointers:
                i.draw()
            turtle.update()


if __name__ == '__main__':
    thing = Drawer(64)
    thing.start()
