'''
Write a program that calculates and prints the bill for a cellular telephone company.  
The company offers two types of service: regular and premium. Its rates vary, depending on the type of service. 
The rates are computed as follows:
 
Regular Service:  

$10.00 plus
First 50 minutes are free, over that, $0.20 per minute.

Premium service:  

$25.00 plus
For calls made from 6:00 a.m. to 6:00 p.m., the first 75 minutes are free, over that, $0.10 per minute.
For calls made from 6:00 p.m. to 6:00 a.m., the first 100 minutes are free, over that, $0.05 per minute.

Your program should prompt the user to enter an account number, a service code, and the number of minutes the service was used. 
A service code of r or R means regular service; a service code of p or P means premium service. Treat any other character as an error. 

Your program should output the account number, type of service, number of minutes the telephone service was used, and the amount due from the user.

For the premium service, the customer may be using the service during the day and the night. 
Therefore, to calculate the bill, you must ask the user to input the number of minutes 
the service was used during the day and the number of minutes the service was used during the night.
'''

#constants
RegularFee = 10.00
PremiumFee = 25.00

#input for account number and the service type
accountNumber = input("What is your account number?\n")
serviceInput = input("What kind of service did you use? (p/r)\n")

#calculate the total service minutes and the amount due
if serviceInput == "r" or serviceInput == "R": #regular service
    serviceMinutes = int(input("How many minutes did you use the service for?\n"))

    if serviceMinutes <= 50:
        amountDue = RegularFee
    elif serviceMinutes > 50:
        amountDue = (serviceMinutes - 50) * .2 + RegularFee

    #output
    print("\nAccount No.", accountNumber, "\nService type: Regular\nService minutes:", serviceMinutes, "\nAmount due: $" + '%.2f'% amountDue)
elif serviceInput == "p" or serviceInput == "P": #premium service
    serviceMinutesDay = int(input("How many minutes did you use the service for during the day?\n"))
    serviceMinutesNight = int(input("How many minutes did you use the service for during the night?\n"))

    if serviceMinutesDay <= 75: #daytime service amount due
        dayDue = 0
    elif serviceMinutesDay > 75:
        dayDue = (serviceMinutesDay - 75) * .10

    if serviceMinutesNight <= 100: #nighttime service amount due
        nightDue = 0
    elif serviceMinutesNight > 100:
        nightDue = (serviceMinutesNight - 100) * .05

    serviceMinutes = serviceMinutesDay + serviceMinutesNight
    amountDue = dayDue + nightDue + PremiumFee

    #output
    print("\nAccount No.", accountNumber, "\nService type: Premium\nService minutes:", serviceMinutes, "\nAmount due: $" + '%.2f'% amountDue)
else: #handle bad inputs
    print("Input invalid.")
