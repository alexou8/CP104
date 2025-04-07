"""
-------------------------------------------------------
Assignment 3, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
from random import randint

def feet_to_acres(square_footage):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = feet_to_acres(square_footage)
    -------------------------------------------------------
    Parameters:
        square_footage - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    
    SQFT = 43560
    
    acres = square_footage / SQFT
    
    return acres

def mow_lawn(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = mow_lawn(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time - time required to mow the lawn in minutes (float)
    ------------------------------------------------------
    """
    
    area = width * length
    time = area / speed
    
    return time

def date_extract(date_number):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extract(date_number)
    -------------------------------------------------------
    Parameters:
        date_number - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    
    year = date_number % 10000
    day = (date_number//10000) % 100
    month = (date_number//10000) // 100
    
    return (year, month, day)

def multiply_fractions(num1, denom1, num2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        num2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        numerator - numerator of the resulting fraction (int)
        denominator - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """
    
    numerator = num1 * num2
    denominator = denom1 * denom2
    product = ((num1/denom1) * (num2/denom2))
    
    return (numerator, denominator, product)

def math_quiz():
    """
    -------------------------------------------------------
    Generates 2 random numbers from 0 to 999 for the user to add and then display the users answer as well as the correct answer.
    Use: math_quiz()
    -------------------------------------------------------
    Parameters:
        
    Returns:
        user_answer - answer the user has entered (int)
        answer - correct answer of the 2 numbers (int)
    ------------------------------------------------------
    """
    
    num1 = randint(0, 999)
    num2 = randint(0, 999)
    
    answer = num1 + num2
    
    print(f"""  {num1:3d}
+ {num2:3d}\n""")
    
    user_answer = int(input("Your answer: "))
    
    print(f"""
Your answer: {user_answer:4d}
Expected:    {answer:4d}""")
    
    return