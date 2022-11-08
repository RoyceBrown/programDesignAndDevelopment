# Written by Royce Brown for ITCS 1140 S1601, Program Design and Development

import time

#print certain phrases in response to user input of a month. break out of
#the while loop for certain inputs
month = ""
while month != "q":
    month = input("Enter a month of the year, or q to quit.\n").lower()
    if month == "december" or month == "january" or month == "february":
        print("It's cold outside!")
        break
    elif month == "march" or month == "april" or month == "may":
        print("Look at the flowers!")
    elif month == "june" or month == "july" or month == "august":
        print("Schools out!")
        break
    elif month == "september" or month == "october" or month == "november":
        print("Look at the harvest moon!")

#prompt the user for a number until they enter a number between -10 and 10.
#once they enter a number in that range, print the number of times they
#were prompted. if that number they entered was even, say so. if it was
#odd, say so. if it was neither, print "I don't know what you entered."
number = float(input("Enter a number between -10 and 10.\n"))
promptCount = 1

while number <= -10 or number >= 10:
    number = float(input("Enter a number between -10 and 10.\n"))
    promptCount += 1

print("You were prompted for a number " + str(promptCount) + " times.")
if number % 2 == 0:
    print("You entered an even number!")
elif number %2 == 1:
    print("You entered an odd number!")
else:
    print("I don't know what you entered.")

#count the number of [aeiou] and [xyz] in a user-inputed string. if the
#string contains the letter m, subtract [xyz] from [aeiou] and print, and
#exit. if the string contains a p, add them, print, and exit. if the string
#contains, neither m nor p, restart the process and prompt for another
out = 0
while out == 0:
    vowelCount = 0
    xyzCount = 0
    mFound = False
    pFound = False

    inputWord = input("Enter a word.\n")

    for letter in inputWord:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            vowelCount += 1
        if letter == "x" or letter == "y" or letter == "z":
            xyzCount += 1
        if letter == "m":
            mFound = True
        if letter == "p":
            pFound = True

    if mFound == True:
        minus = vowelCount - xyzCount
        print(minus)
        out = 1
    if pFound == True:
        plus = vowelCount + xyzCount
        print(plus)
        out = 1

#prompt the user for a number of seconds, then print the number of seconds
#that have elapsed each second until the amount of time entered has passed.
#then print the number of times the loop iterated
timer = 1
seconds = int(input("Enter a number of seconds to wait.\n")) + 1
while timer < seconds:
    time.sleep(1)
    print(str(timer) + " second(s) have elapsed.")
    timer += 1
timer -= 1 #to correct for timer starting on 1

print("The loop iterated " + str(timer) + " times.")
