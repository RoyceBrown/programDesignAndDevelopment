from random import *
from turtle import *

#setup
setup(400,400)
fillcolor('DarkOrange')
bgcolor('khaki')
speed(1)

#setup input
turtleObject = input('What shape do you want your turtle object to be? (classic, arrow, turtle, circle, square, triangle).\n')
shape(turtleObject)
if input('Would you like to play on hardmode? (y/n)\n') == 'y':
    moves = 1
    hardmode = 1
else:
    moves = 10
if input('Would you like to enable the path tracer? (y/n)\n') == 'y':
    tracer = 1


#constant bounds
SpawnXMin = -150
SpawnXMax = 150
SpawnYMin = -150
SpawnYMax = 150

GoalXMin = -100
GoalXMax = 100
GoalYMin = -100
GoalYMax = 100
GoalRMin = 20
GoalRMax = 40

#generate random starting conditions 
spawnX = randint(SpawnXMin, SpawnXMax)
spawnY = randint(SpawnYMin, SpawnYMax)
spawnAzi = 360 * random()

goalX = randint(GoalXMin, GoalXMax)
goalY = randint(GoalYMin, GoalYMax)
goalR = randint(GoalRMin, GoalRMax)

#draw goal
penup()
goalYAdj = goalY - goalR
goto(goalX, goalYAdj)
pendown()
begin_fill()
circle(goalR)
end_fill()

#navigate turtle to it's starting conditions
penup()
goto(spawnX, spawnY)
setheading(spawnAzi)

#variable setup for game loop
azimuth = spawnAzi
win = 0
if tracer == 1:
    pendown()

#game loop
for n in range(moves):
    currentMove = n + 1
    print('You are on move', currentMove, 'of', moves, 'moves.')

    #request azimuth change and set heading
    azimuthChange = int(input('Enter an azimuth to adjust by.\n'))
    right(azimuthChange)
    
    #request distance and move
    distance = int(input('Enter a distance to move.\n'))
    forward(distance)

    currentX = xcor()
    currentY = ycor()

    #check if the win condition is met
    if (currentX - goalX) ** 2 + (currentY - goalY) ** 2 < goalR ** 2:
        win = 1
        break

#check winstate
if win == 1 and hardmode == 1:
    while True:
        speed(6)
        goto(0, 0)
        startAzi = 360 * (random() - .5)
        right(startAzi)
        winDist = randint(20,30)
        winAzi = 45 * (random() - .5)
        for colour in ['red', 'orange', 'yellow', 'green', 'blue', 'purple']:
            color(colour)
            right(winAzi)
            forward(winDist)
            write('You Win!!!', align=('center'), font=('Sitka Small Italic', '12'))
elif win == 1:
    write('You Win!!!', font=('Sitka Small Italic', '16'))
else:
    write('You Lose :(', font=('Sitka Small Italic', '16'))

exitonclick()
