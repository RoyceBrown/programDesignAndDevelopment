# This program takes three numeric inputs and one text input, then uses those to display information about the inputs

print("Hi, my name is Royce Brown and welcome to my Worthless Input Metadata Processor (WIMP).\n")

# input
input1 = int(input("Enter your first number.\n"))
input2 = int(input("Enter your second number.\n"))
input3 = int(input("Enter your third number.\n"))

inputDay = input("Enter a day of the week.\n")

# calculate and output the biggest and smallest of the numerical inputs
biggest = input1
if input2 > biggest:
    biggest = input2
if input3 > biggest:
    biggest = input3

smallest = input1
if input2 < smallest:
    smallest = input2
if input3 < smallest:
    smallest = input3

print("The biggest number is", biggest, "and the smallest number is", str(smallest) + ".")

# calculate and output how many of the numerical inputs are positive or negative
positiveCount = 0
negativeCount = 0
for input in [input1, input2, input3]:
    if input > 0:
        positiveCount += 1
    if input < 0:
        negativeCount += 1

if positiveCount >= 2:
    print("You entered at least 2 positive numbers.")
elif negativeCount >= 2:
    print("You entered at least 2 negative numbers.")
else:
    print("I don't know what you entered.")

# display whether the day entered was a weekday or weekend day
if inputDay == "Monday" or inputDay == "Tuesday" or inputDay == "Wednesday" or inputDay == "Thursday" or inputDay == "Friday":
    print("You entered a weekday.")
elif inputDay == "Saturday" or inputDay == "Sunday":
    print("You entered a weekend day")
else:
    print("You did not enter a day of the week.")

# prints the average of the numerical inputs if the day input was a sunday
if inputDay == "Sunday":
    average = (input1 + input2 + input3) / 3
    print("The average of your three numerical inputs is: {:.2f}".format(average))

# prints the smallest number and day of the week if the the day of the week is monday and the biggest number is greater than or equal to 10
if inputDay == "Monday" and biggest >= 10:
    print("The smallest number was", smallest, "and the day of the week was", inputDay +".")

# prints the biggest number and day of the week if the smalls number is even and less than 50 and the day of the week is wednesday or thursday
if inputDay == "Thursday" or inputDay == "Wednesday" and smallest < 50 and smallest % 2 == 0:
    print("The biggest number is", biggest, "and the day of the week is", inputDay + ".")
