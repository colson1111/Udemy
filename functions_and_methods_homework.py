# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:23:14 2016

@author: Craig
"""

# function that computes the volume of a sphere given its radius
def vol(rad):
    import math
    return (4.0/3) * math.pi * rad**3

vol(2)

# function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    # check if num is between low and high
    if num in range(low,high):
        print "%s is in the range" % str(num)
    else:
        print "The number is outside the range."

ran_check(5, 3, 7)

def ran_bool(num,low,high):
    return num in range(low,high)

ran_bool(3,1,10)



# accepts a string and calculates the number of upper and lower case letters
def up_low(s):
    up_count = 0
    low_count = 0
    
    for i in s:
        if i.isupper():
            up_count += 1
        elif i.islower():
            low_count += 1
        else:
            pass
            
    print "No. of Upper case characters: {p}".format(p = up_count)
    print "No. of Lower case characters: {p}".format(p = low_count)

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')



# takes a list and return a new list with unique elements of the first list
def unique_list(l):
    return set(l)

def unique_list2(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

unique_list2([1,1,1,1,2,2,3,3,3,3,4,5,1,3,'hello',4,2])


# write a python function to multiple all numbers in a list
def multiply(numbers):
    num = 1
    for i in numbers:
        num *= i
    return(num)

multiply([1,2,3,-4])

# write a python function that check if a string is palindrome or not
def palindrome(s):
    return s.upper()[::-1] == s.upper()
       
palindrome('kayak')
palindrome('elephant')


# check whether a string is a pangram or not
import string

def ispangram(str1, alphabet = string.ascii_lowercase):
    letter_count = 0
    
    for i in alphabet:
        if str1.lower().__contains__(i):
            letter_count += 1
        else:
            return False
            break
    if letter_count == 26:
        return True

ispangram("The quick brown fox jumps over the lazy dog")
ispangram("THE QUICK BROWN FOX jumps over the LAZY dog")


def ispangram(str1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())



