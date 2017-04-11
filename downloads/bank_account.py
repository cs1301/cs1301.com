#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW9 - OOP - due Monday, Apr. 17, 2017
"""
__author__ = "YOUR NAME HERE"
__collaboration__ = """ YOUR COLLABORATION STATEMENT HERE """

class BankAccount(object):

    def __init__(self, acct_holder, acct_type, balance = 0):
        """
        Write a constructor for a bank account below.
        The following attributes:
        acct_holder will be a Person object
        acct_type is a string
        balance should be defaulted to 0 if not provided to the constructor, is an int
        """
        pass

    """
    Change Account Type should update Account Type to newType
    """

    def changeAccountType(self, newType):
        pass
    """
    Deposit should update the balance of the bank account depending on amounnt:
    Returns True if deposits,
    False if amount is negative.

    """
    def deposit(self, amt):
        pass

    """
    Withdraw should update the balance of the bank account depending on amount:
    Returns True if withdraws,
    False if amount is negative or there is not enough in the account to withdraw.

    """
    def withdraw(self, amt):
        pass

    """
    Batch Deposit should update the balance of the bank account depending on amounnt:
    Read the file and take all numbers that are alone on a line for deposit.
    Returns True if deposits,
    False if there is no amount.
    """
    def batchDeposit(self, file):
        pass

    """
    Transfer should update the balance of both of the bank accounts depending on amounnt:
    Returns True if deposits,
    False if amount is negative or there is not enough in the account to withdraw from self.
    """
    def transfer(self, other, amt):
        pass

    """
    Greater than compares balances of bank accounts
    Returns True if self is greater,
    False otherwise
    """
    def __gt__(self, other):
        pass


    """
    Less than compares balances of bank accounts
    Returns True if self is less,
    False otherwise
    """
    def __lt__(self, other):
        pass
    """
    Returns True if all attributes are equal, otherwise False
    """
    def __eq__(self, other):
        pass



    """
    Give to charity takes in a list of charities:
    list_charities: BankAccount Objects
    amount: int to donate

    Give the amount to the charities with the smallest balance.
    Split the amount if there is more than 1.

    Update the balances of both the account donating, and the
    charities receiving the donation.

    Return False if there are no charities in the list.
    """
    def giveToCharity(self, list_charities, amount):
        pass

class Person(object):


    """
    Initialize name, age, and wallet
    Initialize account to None
    """
    def __init__(self, name, age, wallet = 0):
        pass


    """
    Start a bank account based on the age of the Person:
    If the age is under 18, add "Youth" to the account type.
    eg: "Youth Savings" if a_type is "Savings"

    Default balance to 0 unless given.

    Update account attribute to this account.
    Note: a Person will have up to one account at any time.
    """
    def startAccount(self, a_type, balance = 0):
        pass


    """
    Update age of Person by 1
    If the age is becomes 18, take away "Youth" from the account type (if there is an account)
    eg: "Savings" if a_type was "Youth Savings"
    """
    def birthday(self):
        pass

    """
    Empty the wallet of the user into the bank account (if exists)
    Update wallet and account balance if applicable
    """
    def emptyWallet(self):
        pass