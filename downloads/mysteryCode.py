#
# mysteryCode.py
#
# A simple interactive script that calculates a secret code based upon student
# input.
# Python 3

def askAge():
    ageInt = 0;
    try:
         age = input("How many years old are you?")
         ageInt = int(age)
    except:
         print("Sorry, that's not a valid answer, try again!")
         ageInt = askAge()
    return ageInt

firstName = input("Hello, what is your first name?")
print( "Hello " + firstName + ", nice to meet you.")
age = askAge()
secretCode = (ord(firstName[0]) + age)  * 2313 

print("Glad to have you in CS 1301! Your secret code is:", secretCode)
