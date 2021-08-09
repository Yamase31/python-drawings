"""
Author: Beth Ann Townsend and James Lawson
Project 8
Name: mondrian.py

This program creates a Mondrian-like painting according to 
the user's input by drawing and filling shapes through Turtle.
"""

import random
import sys
import turtle
from turtle import Turtle, tracer, update

#draws a rectangle using a wire frame
def drawRectangle(t, x1, y1, x2, y2):
    
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.pencolor(red, green, blue)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    

#takes the rectangles from above and fills them with random colors
def fillRectangle(t, x1, y1, x2, y2):
    drawRectangle(t, x1, y1, x2, y2)
    t.fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    t.begin_fill()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()

    
#finally creates the Mondrian-esque painting by putting it all together, taking the user's input level
def mondrian(t, x1, y1, x2, y2, level):
    
    if level > 0:
        if level >= 6:
            tracer(False)
        
        fillRectangle(t, x1, y1, x2, y2)
        #"flips a coin" to decide what sides will be pulled
        vertical = random.randint(1,2)
        portion = random.randint(1,2)

        if portion == 1:
            if vertical == 1:
                mondrian(t, x1, y1, (x2 - x1) // 3 + x1, y2, level - 1)
                mondrian(t, (x2 - x1) // 3 + x1, y1, x2, y2, level - 1)
            else:
                mondrian(t, x1, y1, x2, (y2 - y1) // 3 + y1, level - 1)              
                mondrian(t, x1, (y2 - y1) // 3 + y1, x2, y2, level - 1)
               

        else:
            if vertical == 1:
                mondrian(t, x1, y1, ((x2 - x1) // 3) * 2 + x1, y2, level - 1)
                mondrian(t, ((x2 - x1) // 3) * 2 + x1, y1, x2, y2, level - 1)
            else:
                mondrian(t, x1, y1, x2, ((y2 - y1) // 3) * 2 + y1, level - 1)
                mondrian(t, x1, ((y2 - y1) // 3) * 2 + y1, x2, y2, level - 1)
        
def main():
    
    # Gets the level from the command line argument
    if len(sys.argv) == 1:
        level = 1
    else:
        level = int(sys.argv[1])

    t = Turtle()
    t.speed(0)
    t.hideturtle()
    x = t.screen.window_width() // 2 - 20
    y = t.screen.window_height() // 2 - 20
    mondrian(t, -x, y, x, -y, level)
    # Stop the fly-by window in the terminal
    input("Press enter to quit: ")

if __name__ == "__main__":
    main()


