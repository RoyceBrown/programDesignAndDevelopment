import turtle
import keyboard
import time
from turtle import *

turtle.home
turtle.speed(0)

setup(400,400)

position = [0, 0]
angularVelocity = 0
angularAcceleration = 0

azimuth = 0
velocity = 0
acceleration = 0

drag = .9
angularDrag = .8

metadata = ""

while True:    
    w = keyboard.is_pressed("w")
    s = keyboard.is_pressed("s")
    a = keyboard.is_pressed("a")
    d = keyboard.is_pressed("d")
   
    #pen
    if keyboard.is_pressed(" ") == True:
        pendown()
    elif keyboard.is_pressed(" ") == False:
        penup()

    #turning
    angularAcceleration = (a - d) * (w - s) * abs(velocity)
    angularVelocity = (angularVelocity + angularAcceleration) * angularDrag
    azimuth = azimuth + angularVelocity
    azimuth = azimuth % 360
    turtle.setheading(azimuth)

    #speed
    acceleration = (w - s)
    velocity = (velocity + acceleration) * drag - abs(angularVelocity / 100)
    turtle.forward(velocity)
    '''
    #metadata
    position = turtle.pos()
    turtle.clear()
    metadata = "Azimuth: " + str(azimuth) + "\nAngular Velocity: " + str(angularVelocity) + "\nAngular Acceleration: " + str(angularAcceleration) + "\nPosition: " + str(position) + "\nVelocity: " + str(velocity) + "\nAcceleration: " + str(acceleration)
    goto(-150,-150)
    write(metadata)
    goto(position)
    '''
