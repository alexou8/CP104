"""
-------------------------------------------------------
Assignment 6, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-08"
-------------------------------------------------------
"""
# Imports


def winner():
    """
    -------------------------------------------------------
    Returns two numbers representing how many times the string "blue" and 
    "grey" appeared in the input.
    Use: blue_times, grey_times = winner()
    -------------------------------------------------------
    Parameters:
        NONE
    Returns:
        blues - the number of times "blue" appeared (int)
        greys - the number of times "grey" appeared (int)
    -------------------------------------------------------
    """
    blues = 0
    greys = 0
    answer = "blue"

    while answer == "blue" or answer == "grey":
        answer = input("Enter the winning team: ")
        if answer == "blue":
            blues += 1
        if answer == "grey":
            greys += 1

    return(blues, greys)


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime_check = 0
    check = 2

    while check <= num / 2:
        if num % check == 0:
            prime_check = 1
            break
        check += 1
    if prime_check == 0:
        prime = True
    elif prime_check == 1:
        prime = False

    return prime


def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"Principal:   ${principal:7.2f}")
    print(f"Interest rate: {rate:5.1f}%")
    print(f"Monthly payment: ${payment:.2f}")
    print("""----------------------------------
Month Interest   Payment   Balance
----------------------------------""")

    balance = principal


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """
    count = 0

    if num < 0:
        num = abs(num)

    if num == 0:
        count = 1

    while num > 0:
        count += 1
        num = num // 10

    return count


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """
    total = 0
    factors = 1

    while num != 0 and factors < num:
        if num % factors == 0:
            total = total + factors
            factors = factors + 1
        else:
            factors = factors + 1

    return total
