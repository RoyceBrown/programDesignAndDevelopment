import random

# Design a program that uses a loop to build a list named 
# valid_numbers that contains only the numbers between 
# 0 and 100 from the numbers list below. The program should then
# determine and display the total and average of the values
# in the valid_numbers list.

def problem1():
    print("\n\nProblem 1.\n")

    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    validNumbers = []

    # filter the list for numbers between 0 and 100, inclusive
    for num in numbers:
        if num >= 0 and num <= 100:
            validNumbers.append(num)
    sum = 0

    # calculate average sum
    for num in validNumbers:
        sum += num
    avg = sum / len(validNumbers)

    # output
    print("The total of the valid numbers is", sum)
    print("The average of the valid numbers is %.2f" % avg)


# Design a program that generates a seven-digit lottery number. 
# The program should generate seven random numbers, each in 
# the range of 0 through 9, and assign each number to a
# list element. (Random numbers were discussed in Chapter 5.)
# Then write another loop that displays the contents of the list.

def problem2():
    print("\n\nProblem 2.\n")

    lotteryNumbers = []

    # generate random numbers and enter them into a list
    for num in range(0,7):
        lotteryNumbers.append(random.randint(0,9))

    # output
    for num in lotteryNumbers:
        print(num)
    print(lotteryNumbers)

# Design a program that lets the user enter the total rainfall 
# for each of 12 months into a list. The program should calculate and 
# display the total rainfall for the year, the average monthly rainfall, 
# the months with the highest and lowest amounts.
def problem3():
    print("\n\nProblem 3.\n")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    rainfall = []

    # input and rainfall list generation
    for month in months:
        print("How much rain fell in", month + "?")
        rainfall.append(int(input()))
    
    # calculate total and average rainfall
    totalRain = 0
    for rain in rainfall:
        totalRain += rain
    avgRain = totalRain / len(months)

    # sort for the highest and lowest rainfall months, earlier months
    # have priority. track the month names
    lowestRain = rainfall[0]
    highestRain = rainfall[0]
    lowestMonth = months[0]
    highestMonth = months[0]
    for index in range(len(rainfall)):
        if rainfall[index] < lowestRain:
            lowestRain = rainfall[index]
            lowestMonth = months[index]
        if rainfall[index] > highestRain:
            highestRain = rainfall[index]
            highestMonth = months[index]

    # output
    print("\nThe total rainfall for the year was", totalRain)
    print("The average monthly rainfall was %.2f" % avgRain)
    print("The least rainy month was", lowestMonth, "with", lowestRain, "rain unit(s).")
    print("The most rainy month was", highestMonth, "with", highestRain, "rain unit(s).")

# Design a program that asks the user to enter a series of 20 numbers. 
# The program should store the numbers in a list then display 
# the following data:
# •	 The lowest number in the list
# •	 The highest number in the list
# •	 The total of the numbers in the list
# •	 The average of the numbers in the list

def problem4():
    print("\n\nProblem 4.\n")
    numbers = []

    # take input of 20 numbers and generate a list
    for num in range(0,20):
        print("Enter a number.", "(" + str(num + 1) + "/20)")
        numbers.append(int(input()))
    
    # calculate total and average of the input
    total = 0
    for num in numbers:
        total += num
    avgNum = total / len(numbers)

    # sort for lowest and highest numbers
    lowestNum = numbers[0]
    highestNum = numbers[0]
    for index in range(len(numbers)):
        if numbers[index] < lowestNum:
            lowestNum = numbers[index]
        if numbers[index] > highestNum:
            highestNum = numbers[index]
    
    # output
    print("\nThe total of the numbers is", total)
    print("The average of the numbers is %.2f" % avgNum)
    print("The lowest number is", str(lowestNum) + ".")
    print("The highest number is", str(highestNum) + ".")

# If you have downloaded the source code from the Premium 
# Companion Website you will find a file named charge_accounts.txt 
# in the Chapter 07 folder. This file has a list of a company’s 
# valid charge account numbers. Each account number is a seven-digit 
# number, such as 5658845.
# Write a program that reads the contents of the file into a list. 
# The program should then ask the user to enter a charge account number. 
# The program should determine whether the number is valid by searching 
# for it in the list. If the number is in the list, the program should 
# display a message indicating the number is valid. If the number is not 
# in the list, the program should display a message indicating the 
# number is invalid.

def problem5():
    print("\n\nProblem\n")
    # read the contents of the account file into a list
    infile = open('charge_accounts.txt', 'r')
    accounts = infile.readlines()
    infile.close()
    
    # strip newlines from items in the list
    for index in range(len(accounts)):
        accounts[index] = accounts[index].rstrip('\n')
    
    # check if the input matches one of the numbers from the file
    inputAccount = input("Enter a charge account number.\n")
    numbersMatch = False
    for index in range(len(accounts)):
        if accounts[index] == inputAccount:
            numbersMatch = True
    
    # output
    if numbersMatch == True:
        print("That number is valid!")
    else:
        print("That number is invalid.")

def problem13():
    print("\n\nProblem 13.\n")

    # read the contents of the account file into a list
    infile = open('8_ball_responses.txt', 'r')
    responses = infile.readlines()
    infile.close()    

    # strip newlines from items in the list
    for index in range(len(responses)):
        responses[index] = responses[index].rstrip('\n')
    
    # ask for questions and respond with a random entry until q is entered
    exit = input("What do you ask? (q to quit)\n")
    while exit != "q":
        print(responses[random.randint(0,11)])
        exit = input("What do you ask? (q to quit)\n")

def main():
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
    problem13()

main()