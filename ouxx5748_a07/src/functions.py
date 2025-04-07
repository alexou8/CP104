"""
-------------------------------------------------------
Assignment 7, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-19"
-------------------------------------------------------
"""
# Imports


def list_factors(num):
    """
    -------------------------------------------------------
    Returns the factors of a given number.
    Use: num_factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - given number to find factors (int)
    Returns:
        factors - list of factors of the number (list)
    -------------------------------------------------------
    """
    factors = []

    if num == 0:
        factors.append(0)
    else:
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)

    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    numbers = []
    num = 1

    while num != 0:
        num = int(input("Enter a positive number: "))
        if num > 0:
            numbers.append(num)

    print(numbers)

    return numbers


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: indexes = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    locations = []
    count = 0

    for i in values:
        if target == i:
            locations.append(count)
        count += 1

    return locations


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    ------------------------------------------------------
    """
    temp = list(minuend)

    for i in temp:
        if i in subtrahend:
            minuend.remove(i)

    return None


def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    temp_last = values[0]
    in_order = True
    index = 0

    while in_order and index < (len(values) - 1):
        index += 1
        if values[index] < temp_last:
            in_order = False

        temp_last = values[index]

    if in_order == True:
        index = -1

    return in_order, index
