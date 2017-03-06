#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW7 - Dictionaries - due Monday, Mar. 13, 2017
"""
__author__ = "YOUR NAME HERE"
__collaboration__ = """ YOUR COLLABORATION STATEMENT HERE """

"""
Function name: charCount
Parameters: a string
Returns: a dictionary

Description: Make a function called charCount that takes in a string as a parameter and returns a dictionary. The dictionary should have each character in the string as a key and the corresponding value should be the amount of occurrences of that character.

"""

# ########################### #
# TODO: Function 1: charCount #
# ########################### #


"""
Function name: shopping
Parameters: a dictionary {key is the name of an item (str): value is a tuple containing the item’s cost per unit (float) and how many of that item you want to buy (int)), a list of items that are on sale (str)
Returns: a dictionary {key is the <str> name of an item: value is <float> how much was actually paid for it}

Description: Write a function that takes in a dictionary in which every key is the name of an item, and every value is a tuple with how much the item costs per unit, and how many of the item you want to buy, as well as a list of things that qualify for the store’s 20% off sale. The function should return a dictionary in which every key is the name of an item you bought, and the value is the total amount you paid for that item (i.e. unit price * quantity * .8 if the item is on sale). The dictionary should also have a key-value pair where the key is “total” and the value is the grand total for all of the things you bought.

Notes:
- All prices in the returned dictionary should be rounded to 2 decimal points.
- You can assume that all the items in the list of items on sale will be lowercase. However, not all of the items in the original dictionary will be lowercase.
- You can assume that “total” will never be a key in the original dictionary.

"""
# ########################## #
# TODO: Function 2: shopping #
# ########################## #



"""
Function name: dictReplaceStr
Parameters: a string, a dictionary
Returns: a string

Description: Write a function that takes in a string and a dictionary. The key to dictionary will be a string and the value is another string. In the string, replace every word that is a key in the dictionary with the value that the key maps to and return that new string.

"""

# ################################ #
# TODO: Function 3: dictReplaceStr #
# ################################ #


"""
Function name: groupAge
Parameters: a dictionary {keys are strings: values are dictionaries with member names as keys and their ages as values}
Returns: a dictionary {keys are strings of the group: values are integers with group artists’ ages}

Description: Write a function that takes in a dictionary and returns a dictionary. The function will take in a dictionary where the key will be a string that represents the name of some group and the value will be another dictionary that has the members of the group as the key and their age as the value. The function should take this dictionary and make a new dictionary where the keys will be strings of the group name and the values will be the total of all band member’s ages.

"""
# ########################## #
# TODO: Function 4: groupAge #
# ########################## #


"""
Function name: statistics
Parameters: a list of numbers (ints or floats)
Returns: a dictionary {keys are strings: values are lists or numbers}

Description: Write a function that takes in a list of numbers and returns a dictionary with some basic statistical measures (see table below) about the data in the list.
"""

# ############################ #
# TODO: Function 5: statistics #
# ############################ #