'''
Create a Python program that asks the user for a month as a number between 1 and 12. 
The program should display a message indicating whether the month is in the first quarter, 
the second quarter, the third quarter, or the fourth quarter of the year. 
Following are the guidelines:
If the user enters either 1, 2, or 3, the month is in the "first quarter".
If the user enters a number between 4 and 6, the month is in the "second quarter".
If the number is either 7, 8, or 9, the month is in the "third quarter".
If the month is between 10 and 12, the month is in the "fourth quarter".
If the number is not between 1 and 12, the program should display an error
'''

month = int(input("Enter a number between 1-12 representing a month.\n"))

#test the input for what range it is in
if month == 1 or month == 2 or month == 3:
    quarter = "first quarter"
elif month >= 4 and month <= 6:
    quarter = "second quarter"
elif month == 7 or month == 8 or month == 9:
    quarter = "third quarter"
elif month >= 10 and month <= 12:
    quarter = "fourth quarter"
else:
    quarter = "[invalid month input]"

#output
print("Your month is in the", quarter, "of the year.")