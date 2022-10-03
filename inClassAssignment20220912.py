from turtle import *

#I used numbers based on measuring the image given in Microsoft Paint.

#setup
shape('turtle')
setup(350,350)
speed(10)

#draw blue dot
color('blue')
dot()

#change color to red to draw the other objects
color('red')

#traverse to small square's bottom left corner
penup()
goto(-25,-25)

#draw small red square
pendown()
goto(-25,25)
goto(25,25)
goto(25,-25)
goto(-25,-25)

#traverse to large square's bottom left corner
penup()
goto(-75,-75)

#draw large red square
pendown()
goto(-75,75)
goto(75,75)
goto(75,-75)
goto(-75,-75)

#traverse to bottom left corner and face north
penup()
goto(-125,-125)
setheading(90)
color('blue')

done()