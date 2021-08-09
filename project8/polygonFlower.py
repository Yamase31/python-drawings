"""
Author: James Lawson and Beth Ann Townsend
Project 8
File: polygonFlower.py

This program prompts the user for the side length of a certain polygon of a certain amount, then
it creates a turtle graphic of a flower based on those numbers.
"""

import random
from turtle import Turtle

#this function creates the shapes within the flower that will be created from it below
def drawPolygon(t, lengthSide, flowerShapeNum):
    for count in range(flowerShapeNum):
        t.forward(lengthSide)
        t.left(360/flowerShapeNum)

#compiles the shapes above and draws a flower accordingly, using the user's inputs
def drawFlower(t, lengthSide, numSquares, flowerShapeNum):
    for petals in range(numSquares):
        drawPolygon(t, lengthSide, flowerShapeNum)
        t.left(360/numSquares)


def main():
    #setting up the turtle
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor("blue")
    #prompts the user for the information
    numSquares = 4
    flowerShape = 4
    lengthSide = int(input("Please enter the side length for your flower: "))
    numSquares = int(input("How many shapes do you want your flower to be made of? "))
    flowerShapeNum = int(input("How many sides do you want the shapes to have? "))
    #calls drawFlower to complete the program
    drawFlower(t, lengthSide, numSquares, flowerShapeNum)
    
    
if __name__ == "__main__":
    main()
