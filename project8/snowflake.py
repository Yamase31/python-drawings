"""
Author: James Lawson and Beth Ann Townsend
Project 8
File: snowflake.py

This program draws a Koch snowflake using Turtle after receiving the size and level from the user.
"""
from turtle import Turtle

distance = 0
level = 0
angle = 120

#function that draws one line at a time to create a fractal image
def drawFractalLine(t, level, distance):
    #basecase
    if level == 0:
        t.forward(distance)
    #recursion
    else:
        drawFractalLine(t, level - 1, distance//3)
        t.left(60)
        drawFractalLine(t, level - 1, distance//3)
        t.right(120)
        drawFractalLine(t, level - 1, distance//3)
        t.left(60)
        drawFractalLine(t, level - 1, distance//3)
        
#calls it back
def main(level = 0):
    distance = int(input("Enter your desired snowflake size: "))
    level = int(input("What level do you want your snowflake to be? "))
    #controls the Turtle
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    #draws it three times to form the triangular shape
    drawFractalLine(t, level, distance)
    t.right(angle)
    drawFractalLine(t, level, distance)
    t.right(angle)
    drawFractalLine(t, level, distance)

    
    
if __name__ == "__main__":
    main()
