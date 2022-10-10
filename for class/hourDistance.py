'''The distance a vehicle travels can be calculated as follows:

distance = speed * time
For example, if a train travels 40 miles per hour for three hours, the distance traveled is 120 miles.

Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled. 
It should then use a loop to display the distance the vehicle has traveled for each hour of that time period. 
'''

#take input
speed = int(input('What was the speed of your vehicle, in miles per hour?\n'))
time = int(input("For how long did your vehicle travel, in hours?\n"))

#calculate distance and display hours and distance
for h in range(time):
    hour = str(h + 1)
    distance = (h + 1) * speed
    print('Hour:', hour + ", distance traveled:", distance)
