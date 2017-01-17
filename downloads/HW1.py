#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
Introduction to Functions using Python.
"""
__author__ = "YOUR NAME HERE"
""" YOUR COLLABORATION STATEMENT HERE """

"""
Function name (1): circleArea
Parameters: N/A
Return value: N/A
Description:
Write a Python program which accepts the radius of a circle from the user and compute the area.
1.  Ask the user to input the radius of the circle.
2.  In geometry, the area enclosed by a circle of radius r is [pi]r2. Calculate the area, round it to two three points and print a descriptive prompt. (Ex. The area of the circle with radius 1.1 is 3.801 )
Hints:
-   You can round a number by using the round(number, number of decimal places) function or by using string formatting. For example, you can round 56.789 to 56.79 by using round(56.789,2).
-   Importing the math module to get the value of [pi] might be helpful.
"""

# ######################### #
# TODO: Write function here #
# ######################### #

"""
Function name (2): howManyLegs
Parameters: N/A
Return value: N/A
Description:
Write a function that takes the number of chickens, tarantulas, and horses a person owns and calculates the number of total legs among all the animals.
1.  Get the number of chickens the user owns; multiply the number by 2.
2.  Get the number of tarantulas the user owns; multiply this number by 8.
3.  Get the number of horses the user owns; multiply this number by 4.
4.  Add all these numbers together and print the total in a descriptive format. (Ex. 4 chickens, 2 tarantulas, and 6 horses have 48 legs. )
"""

# ######################### #
# TODO: Write function here #
# ######################### #

"""
Function name (3): calcBMI
Parameters: N/A
Return value: N/A
Description:
Write a function that takes in a person's height and weight and calculates a person's body mass index (BMI).
1.  Get the person's weight in pounds from the user; make sure to use a descriptive prompt so the user knows what units to use.
2.  Get the person's height in inches from the user; again, make sure to use a descriptive prompt so the user knows what units to use.
3.  Calculate the person's BMI as following:
a.  Multiply the person's weight by .45 to convert it to kilograms.
b.  Multiply the person's height by .025 to convert it to centimeters, then square the result.
c.  Divide the result from step a by the result from step b.
d.  Print out the calculated BMI, rounded to one decimal place, in a descriptive format. (Ex. A person who weighs 140 pounds and is 66 inches tall has a BMI of 23.1.)
"""

# ######################### #
# TODO: Write function here #
# ######################### #


"""
Function name (4): publix
Parameters: N/A
Return value: N/A
Description:
Rachel is going to Publix and only has a set amount of money. She wants to spend it wisely by buying as many expensive items as she can until she runs out of money. The items are priced as:
1.  Chicken Wings: $13
2.  Taquitos: $6
3.  Coke: $4
4.  Chips: $2
5.  Mints: $1
Write a function that asks the user how much money they have with them and calculate what she can buy at the store.
1.  Ask the user how much money they have.
2.  Calculate how many of each item they can purchase giving priority to the more expensive items.
3.  Print out a statement with the calculated number of items on one line, and be sure to add labels to the values so the user knows what the value means.
(Ex: With $33 they can buy 2 chicken wings, 1 taquitos, 0 coke, 0 chips, and 1 mints.)
Hints:
-   The modulus (%) and integer division (//) operators will be very useful for this function.
Test Cases (not an exhaustive list):
-   With $33 they can buy 2 chicken wings, 1 taquitos, 0 coke, 0 chips, and 1 mints.)
-   With $14 they can buy 1 chicken wings, 0 taquitos, 0 coke, 0 chips, and 1 mints
-   With $26 they can buy 2 chicken wings, 0 taquitos, 0 coke, 0 chips, and 0 mints
-   With $11 they can buy 0 chicken wings, 1 taquitos, 1 coke, 0 chips, and 1 mints
"""

# ######################### #
# TODO: Write function here #
# ######################### #

"""
Function name (5): tipCalc
Parameters: N/A
Return value: N/A
Description:
Write a function that takes the price of a restaurant meal, asks the user how much they want to tip, and calculates the amount they should leave as tip.
1.  Get the price of the meal in dollars and cents from the user; make sure to use a descriptive prompt so the user knows what units to use.
2.  Ask the user how many percent they want to tip. If they want to tip 15%, they should enter: 15. (Assume an integer percentage i.e. giving a 15.5% tip is not allowed)
3.  Print a descriptive statement of your calculations (see test cases for formatting).
Test Cases (not an exhaustive list):
-   If your meal was: $11.0 and you want to give a 18% tip. The tip will be: $1.98, so the new total is: $12.98
-   If your meal was: $24.5 and you want to give a 20% tip. The tip will be: $4.9, so the new total is: $29.4
-   If your meal was: $30.9 and you want to give a 15% tip. The tip will be: $4.63, so the new total is: $35.53
"""
# ######################### #
# TODO: Write function here #
# ######################### #

"""
Function name (6): compound_interest
Parameters: N/A
Return value: N/A
Description:
The formula for computing the final amount if one is earning compound interest is given as:
    [ CHECK PDF ]
Calculate the total amount of earning compound interest. Input from the user all the information needed to make your calculations.

Test Cases (not an exhaustive list):
-   With an initial investment of $10000.0, an 8.0% annual nominal interest rate, compounded 1 times per year after 5 years you will have a final amount of: $14693.28.
-   With an initial investment of $1500.0, an 3.0% annual nominal interest rate, compounded 1 times per year after 10 years you will have a final amount of: $2015.87.
"""
# ######################### #
# TODO: Write function here #
# ######################### #

"""
Function name (7): main
Parameters: N/A
Return value: N/A
Description:
This function has been started for you. It serves as an introduction for conditional statements (learned later in the course). All you have to do is ask the user what function they will like to call and make the function call yourself.
1.  Ask the user to input the number of the function [1-6]
2.  Replace the pass statements with your function calls.
"""
def main():
    # TODO: finish this function (replace the pass with function calls)#

    ans = None #replace None with input to user
    if  ans == 1:
        pass
    elif ans == 2:
        pass
    elif ans == 3:
        pass
    elif ans == 4:
        pass
    elif ans == 5:
        pass
    elif ans == 6:
        pass
    else:
        print("Invalid Function.")