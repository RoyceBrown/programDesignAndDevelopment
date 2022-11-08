#functions

#prints a nice looking header
def introduction():
    print("+-----------------------------------+\n| Welcome to my Morse Code program! |\n+-----------------------------------+\n")

#takes user input of a word. input is restricted to strings 
#using only the first six letters of the alphabet
def getWord():
    word = input("Enter a word to be converted into Morse code. (only letters [abcdef] will be used)\n").lower()
    return word

#converts the user input string into morse code, 
#using hyphens and periods as data characters and spaces 
#marking the end of each character
def convertWordToCode(inputWord):
    morseWord = ""

    for letter in inputWord:
        if letter == "a":
            morseWord += ".- "
        elif letter == "b":
            morseWord += "-... "
        elif letter == "c":
            morseWord += "-.-. "
        elif letter == "d":
            morseWord += "-.. "
        elif letter == "e":
            morseWord += ". "
        elif letter == "f":
            morseWord += "..-. " 

    return morseWord

#converts the morse-converted user input back into plaintext. 
#this builds up each morse letter in a local string until a space 
#is reached, then tests what character that morse letter corresponds to.
#it is pretty neat
def convertCodeToWord(plainMorse):
    wordMorse = ""
    letterBuild = ""

    for symbol in plainMorse:
        if symbol == " ":
            if letterBuild == ".-":
                wordMorse += "a"
                letterBuild = ""
            elif letterBuild == "-...":
                wordMorse += "b"
                letterBuild = ""
            elif letterBuild == "-.-.":
                wordMorse += "c"
                letterBuild = ""
            elif letterBuild == "-..":
                wordMorse += "d"
                letterBuild = ""
            elif letterBuild == ".":
                wordMorse += "e"
                letterBuild = ""
            elif letterBuild == "..-.":
                wordMorse += "f"
                letterBuild = ""
        else:
            letterBuild += symbol

    return wordMorse

#count the number of dots and dashes and calculate the ratio between them
#i handle this a bit differently than the assignment calls for for
#aesthetic reasons.
def analytics(plainMorse):
    dots = 0
    dashes = 0.000001 #this is set to a small number to prevent a divide by zero error

    for symbol in plainMorse:
        if symbol == ".":
            dots += 1
        elif symbol == "-":
            dashes += 1

    ratio = dots / dashes #if no dashes are present, this will return a large number

    return ratio, dots, dashes

#prints the reconverted input word, the morse code conversion, the ratio, 
#and the number of dots and dashes in a neat fashion
def prettyPrint(plainWord, plainMorse, ratio, dots, dashes):
    formatRatio = "{:.2f}".format(ratio)
    formatDashes = "{:.0f}".format(dashes)
    print("+------------------------------------------>\n|        Your word was: " + plainWord + "\n| and in Morse code is: " + plainMorse + "\n| which has " + str(dots) + " dots, " + formatDashes + " dashes,\n| and " + formatRatio + " dots per dash." + "\n+------------------------------------------>")

#execute functions and chain them together, then produce the output
def main():
    introduction()
    inputWord = getWord()
    morse = convertWordToCode(inputWord)
    outputWord = convertCodeToWord(morse)
    ratio, dots, dashes = analytics(morse)
    prettyPrint(outputWord, morse, ratio, dots, dashes)

#run main
main()