'''
Create a Python program that prompts the user to enter an integer. 
The program should display “Positive” if the number is greater than 0, “Negative” if the number is less than 0, and “Zero” if the number is equal to 0. 
The program should then display “Even” if the number is even, and “Odd” if the number is odd.
'''

#setup
userInput = int(input("Enter an integer.\n"))
sign = ""
parity = ""

#test for sign
if userInput > 0:
    sign = "positive"
elif userInput == 0:
    sign = "zero"
elif userInput < 0:
    sign = "negative"

#test for parity
userInputMod2 = userInput%2
if userInputMod2 == 0:
    parity = "even"
elif userInputMod2 == 1:
    parity = "odd"

#output
print("Your number is", sign, "and", parity)
