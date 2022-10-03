'''
Written by Royce Brown.

Spherical Inc. sells baseballs for $1.99 each. However, discounts are given according quantities listed in the following table:

Quantity	Discount
0 - 9    	0%
10 - 50	    5%
51 or more 	10%


Develop a Python program that prompts the user to enter the number of baseballs purchased.
The program should ask the user if they want giftwrapping and if so add another $2.00 to the order.
The program should display the amount of the discount (if any) and the total amount of the purchase 
after the discount and including the giftwrapping if needed.
Include tax of 6% on the total of the purchase, excluding giftwrapping.
'''

#constants
BasePrice = 1.99
WrappingPrice = 2.00
Tax = 1.06
DiscountTier0 = .0
DiscountTier1 = .05
DiscountTier2 = .1

#inputs
quantity = int(input("How many baseballs have you purchased?\n"))
giftWrapping = input("Do you want giftwrapping? (y/n)\n")

#converts wrapping input to a number
if giftWrapping == "y":
    giftCharge = WrappingPrice
else:
    giftCharge = 0

#test for number of baseballs purchased
if quantity >= 0 and quantity <= 9:
    discountPercent = DiscountTier0
elif quantity >= 10 and quantity <=50:
    discountPercent = DiscountTier1
elif quantity >= 51:
    discountPercent = DiscountTier2

#calculate the amount of discount and the final price
realPrice = quantity * BasePrice
discount = realPrice * discountPercent
finalPrice = Tax * (realPrice - discount) + giftCharge

#output
print("You saved $" + '%.2f'% discount, "on your purchase.")
print("The final charge is $" + '%.2f'% finalPrice + ".")
