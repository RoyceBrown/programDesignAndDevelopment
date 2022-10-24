'''Create a Python module that implements the 4 functions needed for a simple calculator. The functions required are:

Add - This function takes 2 numbers and returns the result of the operation
Subtract - This function takes 2 numbers and returns the result of the operation
Multiply - This function takes 2 numbers and returns the result of the operation
Divide - This function takes 2 numbers and returns the result of the operation
Welcome - This function welcomes the user to the program
main - This is a glue function that connects the other functions and variables together'''

#define all operation modules
def add(num1, num2):
    sum = num1 + num2
    return sum

def subtract(num1, num2):
    difference = num1 - num2
    return difference

def multiply(num1, num2):
    product = num1 * num2
    return product

def divide(num1, num2):
    dividend = num1 / num2
    return dividend

#header module
def welcome():
    print("Royce Brown's Basic Calculator\n")

def main():
    welcome()

    #variable input
    value1 = int(input("Input your first value.\n"))
    value2 = int(input("Input your second value.\n"))

    #input operation type, with input checking
    exit = 0
    while exit == 0:
        operation = input("What operation do you wish to execute? Accepted inputs are: + , - , * , /\n")
        if operation == "+":
            result = add(value1, value2)
            exit = 1
        elif operation == "-":
            result = subtract(value1, value2)
            exit = 1
        elif operation == "*":
            result = multiply(value1, value2)
            exit = 1
        elif operation == "/":
            result = divide(value1, value2)
            exit = 1
        else:
            print("That input is invalid.")

    #output
    print(value1, operation, value2, "=", str(result) + ".")

main()