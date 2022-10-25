'''Using Python Turtle create a program to draw a traffic light using user defined Python functions.

The functions required are:

DrawCircle - This function takes the values required to draw a circle at the indicated coordinates and radius 
DrawRectangle - This function takes the values required to draw a rectangle at the indicated coordinates and length and width 
DrawTrafficLight - This is a glue function that connects the other functions and variables together
main - This function will call the DrawTrafficLight function at 3 different locations and therefore draw 3 traffic lights
Note: When designing the program, think about the percentage of sizes instead of absolute sizes.'''

from turtle import *

#draw circle with center at input coordinates
def drawCircle(x, y, radius, color):
    #navigate to the southern point of the circle
    goto(x, y - radius)
    pendown()

    #draw circle
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()
    penup()

#draw rectangle with center at input coordinates
def drawRectangle(x, y, height, width):
    #navigate to the bottom left corner of the rectangle
    goto(x - width / 2, y - height / 2)
    pendown()

    #draw rectangle
    goto(x - width / 2, y + height / 2)
    goto(x + width / 2, y + height / 2)
    goto(x + width / 2, y - height / 2)
    goto(x - width / 2, y - height / 2)
    penup()

#draw a rectangle at the given centerpoint with a width and height large enough to 
#fit the circles with equal amount of space between each circle and the rectangle's sides.
#then draw three circles with traffic light fill colors at equally space points in the rectangle.
#the r parameter is the radius of the circle, and the d parameter is the distance between each circle and
#the rectangle sides.
def drawTrafficLight(x, y, r, d):
    drawRectangle(x, y, 6 * r + 4 * d, 2 * r + 2 * d)
    drawCircle(x, y + 2 * r + d, r, "red")
    drawCircle(x, y, r, "yellow")
    drawCircle(x, y - 2 * r - d, r, "green")

def main():
    #setup
    setup(800, 800)
    width(3)
    hideturtle()
    penup()

    #draw three traffic lights, with varying sizes and proportions
    drawTrafficLight(100, 100, 15, 25)
    drawTrafficLight(0, 0, 25, 25) 
    drawTrafficLight(-200, -100, 25, 15)    
    exitonclick()

main()
