"""
-------------------------------------------------------
Assignment 5, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports

def factorial(num):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of num.
    Use: product = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - number to factorial (int > 0)
    Returns:
        product - num! (int)
    ------------------------------------------------------
    """
    
    product = 1
    
    for i in range(1, num+1):
        product = product * i
    
    if num == 0:
            product = 0
    
    return product

def calories_burned(per_minute, minutes):
    """
    -------------------------------------------------------
    Calculates and returns the amount of calories burned
    every 5 minutes up to a total amount of minutes.
    Use: total_burned = calories_burned(calories_min, mins)
    -------------------------------------------------------
    Parameters:
        calories_min - calories burned per minute (float)
        mins - total time on treadmill (int)
    Returns:
        NONE
    ------------------------------------------------------
    """
    
    if per_minute == 0 and minutes == 0 or minutes == 0:
        print("You did not burn any calories")
    
    calories = per_minute * 5
    count = 1
    
    for i in range(5, minutes+5, 5):
        show_calories = calories * count
        print(f"{i:3d}:{show_calories:7.1f}")
        count = count + 1
    
    return

def open_triangle(num_rows):
    """
    -------------------------------------------------------
    Prints a open triangle with a given number of rows 
    using the character "#". 
    Use: open_triangle(num_rows)
    -------------------------------------------------------
    Parameters:
        num_rows - number of characters wide (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in range(0, num_rows):
        for j in range(0, i+2):
            if j == 0 or j == i+1:
                print('#', end = "")
            else:
                print(" ", end = "")
        print()
    
    return

def multiplication_table(start, stop):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start to stop.
    Use: multiplication_table(start, stop)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        stop - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    
    print("      ", end = " ")
    
    for i in range(start, stop+1):
        print(f"{i:5d}", end = "")
    print()
        
    print("      ", end = " ")
    
    for i in range(start, stop+1):
        print("-----", end = "")
    print()
    
    for i in range(start, stop+1):
        print(f"{i:5d} |", end = " ")
        for j in range(start, stop+1):
            print("{:4d}".format (i * j), end = " ")
        print()
        
    return
         
def range_total(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start by increment.
    Use: total = range_total(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    
    end = start + (increment * count)
    total = 0
    
    if increment == 0:
        total = 0
    else:
        for i in range(start, end, increment):
            total = total + i
    
    return total