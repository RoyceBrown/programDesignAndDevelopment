'''
Create a Python program called "Character Analyzer" that will prompt the user 
for an integer and return the ascii character.

space
non-printable or printable
numbers
upper or lowercase
'''

#input
asciiInput = int(input("Enter an ASCII number.\n"))

#output
asciiPrintable = chr(asciiInput)
print("Your character is:", asciiPrintable + ".")

#test for different ranges that the character falls in, each range being assigned a group. 
#for capital and lowercase letters, the alternate forms of the letters are also returned
if asciiInput >= 0 and asciiInput <= 31:
    print("This character is a control character.")
elif asciiInput >= 33:
    print("This character is printable.")

if asciiInput == 32:
    print("This character is a space.")
elif asciiInput >= 33 and asciiInput <=47 or asciiInput >= 58 and asciiInput <=64 or asciiInput >= 91 and asciiInput <=96 or asciiInput >=123:
    print("This is a special character.")
elif asciiInput >=48 and asciiInput <=57:
    print("This character is a digit")
elif asciiInput >= 65 and asciiInput <= 90:
    print("This character is a capital letter.")
    altCharacter = chr(asciiInput + 32)
    print("The lowercase version of your letter is", altCharacter + ".")
elif asciiInput >= 97 and asciiInput <= 122:
    print("This character is a lowercase letter.")
    altCharacter = chr(asciiInput - 32)
    print("The uppercase version of your letter is", altCharacter + ".")
