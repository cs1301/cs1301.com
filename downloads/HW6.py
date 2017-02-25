#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW6 - File I/O - due March 02, 2017
"""
import csv
import urllib.request
import urllib.parse
from datetime import datetime

__author__ = "YOUR NAME HERE"
__collaboration__ = """ YOUR COLLABORATION STATEMENT HERE """

#######################
#       PART 1        #
#   File Manipulation #
#######################

"""
You have been provided with a text file. You can download it here: http://cs1301.com/downloads/RamblinWreck.txt Read the file and replace all instances of ‘engineer’ with title<str>. If title<str> begins with a consonant, then the ‘an’ before the title<str> should be replaced with ‘a’. Also, indent all lines that do not contain the word ‘engineer’ (in the original file). The improved fight song is written to a new file. Name this file: ImprovedFightSong.txt
"""
def improve_fight_song(title):
    pass

"""
Maintain an active log of a chat history by writing the information to a text file. Name your file: log.txt. You should write information about the message. Include the time, determined by the value passed in via the time<datetime.datetime> parameter. Also include the sender<str>, the
receiver<str>, and finally the message, msg<str>. Check the test cases for exact format.
"""
def my_chat(sender, receiver, msg, time = datetime.now()):
    pass

"""
Writes a file containing the information in the list sorted by artist_name<str>. The songs by an artist should be written to the file in a numbered list. The function can handle any number of tuples. The name of the file being created is songInfo.txt.
"""
def song_by_artist(songs):
    pass


#########################
#         PART 2        #
# CSV and Data Analysis #
#########################

"""
Returns a list of the top N<int> company_names<str> in a given year<int>.
If N > length of list for given year, return all company_names ranked that year.
"""
def top_companies(year, N):
    pass

"""
Returns a tuple (rank<int>, revenue(millions)<float>, profit (millions)<float>) of the company_name for the given year. Return None if the company was not ranked that year
"""
def company_ranking(company_name, year):
    pass

"""
Returns a tuple (average<float(2 decimals)>, count<int>) of the company_name. Where average<float> is the average ranking a given company over all the years. Where count<int> is the number of times the company has been in the ranking. Return None if the company has not been
"""
def company_average(company_name):
    pass

#######################
#       PART 3        #
#       urllib        #
#######################

def format_url(url, msg):
    """ Returns a safe url for opening using urllib """
    return url+"?str={}".format(urllib.parse.quote(msg))

main_url = "http://cs1301.com/"

def encrypt_message(msg):
    """ Returns an encrypted message. """
    pass

def decrypt_message(msg):
    """ Returns the decrypted message. """
    pass

########################
#        PART 4        #
#     Extra Credit     #
# Concurrent Functions #
########################

"""
Write a function that, on an infinite cycle, opens the file given as an argument, checks for new lines, and prints anything that has not been printed yet.
"""
def my_chat_listen(filename):
    pass

"""
Write a function that, on an infinite cycle, asks the user for input and writes the input to
"""
def my_chat_send(filename):
    pass