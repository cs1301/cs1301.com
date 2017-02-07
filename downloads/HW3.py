#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
Introduction to Functions using Python.
"""
__author__ = "YOUR NAME HERE"
""" YOUR COLLABORATION STATEMENT HERE """


"""
Function name (1): countLetter
Parameters: string to iterated through (str), letter to count occurances of (str)
Return value: number of the given letter appears in the string (int)
Description:
Write a function that takes in two parameters, one being a string of any length, and the other being an individual letter to count the occurrences of.
1. Uppercase and lowercase letters should both be counted. If the letter does not appear in the sentence, return 0.
2. Must use a for-each loop.
"""

# ######################### #
# TODO: Write function here #
# ######################### #


"""
Function name (2): encryptMessage
Parameters: string to encrypt (str)
Return value: encrypted string (str)
Description:
You are working on a top secret project for which you have to encrypt words that come through. Write a function that takes in the word to be encrypted as a parameter and returns the encrypted word. The rules for encryption are as follows:
    1. “a” or “A” → “@”
    2. “s” or “S” → “$”
    3. “h” or “H” → “#”
    4. Numbers should not be included in the encrypted string
    5. “!” indicates to stop the encryption
"""

# ######################### #
# TODO: Write function here #
# ######################### #


"""
Function name (3): encryptSentence
Parameters: sentence to encrypt (str)
Return value: encrypted sentence (str)
Description:
For the same top secret project, you are sometimes posed with the problem of encrypting sentences.
To encrypt a sentence, only words that begin with a capital letter should be encrypted.
You should call your encryptMessage() from above to encrypt words in the sentence.
"""

# ######################### #
# TODO: Write function here #
# ######################### #


"""
Function name (4): stringPartition
Parameters: a word (str)
Return value: modified word (str)
Description:
Write a function that takes in a word as a parameter and returns a modified version of the word
in which all letters at an even index are in the first half of the string and all letters at
an odd index are in the second half of the string. The letter at index 0 should be the first letter in the modified word.
"""

# ######################### #
# TODO: Write function here #
# ######################### #


"""
Function name (5): sumEvens
Parameters: upper-bound for range (int)
Return value: sum of evens within the range 0 to upper-bound
Description:
1. Write a function that accepts an upper bound from a range from zero to that upper-bound. That upper bound is not included in the range.
2. After calculating the range, your function should sum up all even values within the range.
"""

# ######################### #
# TODO: Write function here #
# ######################### #


"""
Function name (6): vowelsAndConsonants
Parameters: original word (str)
Return value: original word ordered by vowels and consonants
Description:
Write a function that takes a string as a parameter, and separates the vowels and consonants from one another.
1. It should return one string, consisting of the same letters of the original string, but with all of the vowels at the front of the string,
2. All of the consonants should be at the back of the string. Must iterate through the string.
Hints:
- String concatenation might help for this function.
"""

# ######################### #
# TODO: Write function here #
# ######################### #

"""
Function name: guessNumber
Parameters: final answer (int)
Return value: number of guesses the user took (int)
Description:
Write a function that takes an integer value in and asks the user to try to guess this answer. When the user guesses the correct value, print a congratulatory statement and tell them how many guesses it took. If the user inputs “quit” (exactly the string quit, don’t worry about edge cases like ‘QUIT’), your code should end, and print the correct answer. The integer returned if the user quits should be -1. You must use a while-loop.

Here are some test cases to show you how the function should work:

    >>> a = guessNumber(5)
    >>> “What is your guess?” —›  2
    >>> “Wrong answer, try again” —›  4
>>> “Wrong answer, try again” —›  5
      >>> “Correct! It took you 3 tries.”
_____________________________________
>>> print(a)
      >>> 3

    >>> a = guessNumber(5)
    >>> “What is your guess?” —›  2
    >>> “Wrong answer, try again” —›  4
>>> “Wrong answer, try again” —›  quit
      >>> “The correct answer was 5.”
_____________________________________
>>> print(a)
      >>> -1


"""

# ######################### #
# TODO: Write function here #
# ######################### #


"""
Function name (8): diamond
Parameters: a number 2-9 specifying half the width of the diamond (int)
Return value: N/A
Description:
Write a function that takes in a number specifying half the width of the diamond as a parameter and prints a diamond of those specifications.
Make sure the diamond prints in the correct format as shown in the example below. Do not hardcode this. You must use a for-loop.
"""

# ######################### #
# TODO: Write function here #
# ######################### #


"""
Function name (9): countDivisibility
Parameters: lower-bound value (int), upper-bound value (int)
Return value: N/A
Description:
1. Write a function that takes two parameters as the lower and upper bound of a range of intervals.The upper bound is not inclusive.
2. Within this range, your code should count the number of values that are either only divisible by 3, only divisible by 5, or divisible by both 3 and 5.
Each value can only satisfy one circumstance. For example, 15 can only be counted towards being divisible by both 3 and 5.
3. Your code should then print the counts of divisibilities in an informative way.

"""

# ######################### #
# TODO: Write function here #
# ######################### #



"""
Function name (10): multiTable
Parameters: number to make the multiplication table for (int)
Return value: N/A
Description:
Write a function that takes in a number as a parameter and prints the multiplication table for that number.
The table should be printed in an easy to read format.
The first row and column should display the numbers from 1 – number specified.
The top left corner of the table should remain blank as shown in the example below.
Do not hard code this. You must use a for-loop.
"""

# ######################### #
# TODO: Write function here #
# ######################### #

