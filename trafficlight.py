from turtle import *

#values based on pixel approximations of the image given, then quantized to increments of 40.

setup(240, 480)
hideturtle()
speed(9)
pensize(5)


#navigate to lower left corner of border
penup()
goto(-80,-200)

#draw border
pendown()
goto(80,-200)
goto(80,200)
goto(-80,200)
goto(-80,-200)


#draw green circle
penup()
goto(0,-160)
pendown()
fillcolor('green')
begin_fill()
circle(40)
end_fill()

#draw yellow circle
penup()
goto(0,-40)
pendown()
fillcolor('yellow')
begin_fill()
circle(40)
end_fill()

#draw red circle
penup()
goto(0,80)
pendown()
fillcolor('red')
begin_fill()
circle(40)
end_fill()

done()