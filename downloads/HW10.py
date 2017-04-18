#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW10 - Recursion - due Monday, Apr. 24, 2017
"""
__author__ = "YOUR NAME HERE"
__collaboration__ = """ YOUR COLLABORATION STATEMENT HERE """

"""
Function name: multiply
Parameters: an integer, an integer
Returns: an integer

Description: Write a function called multiply that takes in two integer parameters and returns the result of the two parameters multiplied together. You may not use the multiplication operator (*) or any sort of iteration. You must use the addition operator and recursive calls. You do not have to account for negative numbers, but one of the parameters may be zero.

Test cases:
>>> multiply(2, 5)
10
>>> multiply(3,0)
0

"""
def multiply(a,b):
    #YOUR CODE HERE
    pass

"""
Function name: findLength
Parameters: string, list, or tuple
Returns: integer

Description: Write a function called findLength that accepts one parameter that is either a list, string, or tuple. Use recursion to find the length of the data type. You may use the len() function only once, and you may only use the len() function to check if the parameter length is zero. You will get no credit for simply returning len(parameter) and not finding the length using recursive calls.


Test cases:
>>> findLength("Moana")
5
>>> findLength((5, 7, True, ["ok", "now"]))
4
>>> findLength([])
0
"""
def findLenght(item):
    #YOUR CODE HERE
    pass

"""
Function name: triangular
Parameters: integer
Returns: a list

Description: Write a function called triangular that accepts one integer parameter that returns a list with the same number of terms as the value of the parameter. If the parameter is zero or a negative number, you should return an empty list.

A triangular number is the sum of a positive integer and all the integers before it. The series is as follows: 1, 3, 6, 10, 15, 21, ...

Test cases:
>>> triangular(3)
[1, 3, 6]
>>> triangular(5)
[1, 3, 6, 10, 15]
>>>triangular(-2)
[]
"""
def triangular(num):
    #YOUR CODE HERE
    pass

"""
Function name: sumList
Parameters: a list
Returns: integer

Description: Write a function called sumList that accepts one parameter, a list of integers and sub-lists containing integers. Using recursion, you must return the sum of all the integers in all the lists. No iteration (for or while loops) allowed.

Test cases:
>>> sumList([4, 10, 3])
17
>>> sumList([2, 4, [[2, 1], 6]])
15
>>> sumList([])
0
>>> sumList([[8], 3, [1, 1, [1, [3, -5]]]])
12
"""
def sumList(aList):
    #YOUR CODE HERE
    pass

"""
Function name: findIndex
Parameters: a list (guaranteed to be sorted), and integer
Returns: integer

Description: Write a function called findIndex that accepts two parameters, a sorted list of numbers and a target number (numbers can be integers or floats.) Use recursion to implement binary search on the sorted list of numbers and return the index of the target if it is in the list, or -1 if it is not in the list.

Test cases:
>>> findIndex([3, 5, 7, 9, 20], 9)
3
>>> findIndex([4, 5, 6.2], 4)
0
>>> findIndex([1, 2, 3], 10)
-1
"""
def findIndex(aList, target):
    #YOUR CODE HERE
    pass
