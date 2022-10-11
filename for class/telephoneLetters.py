'''Using letters as the telephone number is frequently used. 
So, for instance the words GOT-MILK can be converted to the phone number 468-6455. 

Write a Python program that asks the user to enter a telephone number 
as letters and then outputs the corresponding telephone number in digits.

The program should output the '-' after the third digit. 
The program should accept both upper- and lower-case letters, and spaces. '''

#take input
exit = 0
while exit == 0:
    inputText = input("Enter a seven letter long telephone code, with a dash included.\n").lower()
    if len(inputText) != 8:
        print("That input is invalid.")
    else:
        exit = 1

#convert the input to a phone number
accumulator = ''
for letter in inputText:
    if letter >= 'a' and letter <= 'c':
        currentNum = '2'
    elif letter >= 'd' and letter <= 'f':
        currentNum = '3'
    elif letter >= 'g' and letter <= 'i':
        currentNum = '4'
    elif letter >= 'j' and letter <= 'l':
        currentNum = '5'
    elif letter >= 'm' and letter <= 'o':
        currentNum = '6'
    elif letter >= 'p' and letter <= 's':
        currentNum = '7'
    elif letter >= 't' and letter <= 'v':
        currentNum = '8'
    elif letter >= 'w' and letter <= 'z':
        currentNum = '9'
    elif letter == ' ':
        currentNum = ' '
    else:
        currentNum = '-'
    accumulator += currentNum

#print the output
print("The phone number is", accumulator + ".")
