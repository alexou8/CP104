"""
-------------------------------------------------------
Lab 6, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-24"
-------------------------------------------------------
"""
# Imports

# Constants

def sum_partial_harmonic(n):
    """
    -------------------------------------------------------
    Sums and returns the total of a partial harmonic series.
    This series is the sum of all terms 1/i, where i ranges
    from 1 to n (inclusive)
    i.e. 1 + 1/2 + 1/3 + ... + 1/n
    Use: total = sum_partial_harmonic(n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int > 0)
    Returns:
        total - sum of partial harmonic series from 1 to n (int)
    ------------------------------------------------------
    """
    
    total = 0
    
    for i in range(1, n+1):
        total = total + 1/i
    
    return total

def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    
    for i in range(width):
        for j in range(i+1):
            if j == 0 or j == i or i == width-1:
                print(f'{char}', end = "")
            else:
                print(" ", end = "")
        print()
    
    return

def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    
    if n == 1:
        bottles = 'bottle'
        bottles_minus = 'bottles'
    elif n == 2:
        bottles = 'bottles'
        bottles_minus = 'bottle'
    else:
        bottles = 'bottles'
        bottles_minus = 'bottles'
        
    for i in range(n, 2, -1):
        print(str(n) + " " + bottles + " of beer on the wall, " + str(n) + " " + bottles + " of beer.")
        print("Take one down, pass it around, " + str(n-1) + " " + bottles_minus + " of beer on the wall.")
        print(" ")
        n -= 1
    
    print("""2 bottles of beer on the wall, 2 bottles of beer.
Take one down, pass it around, 1 bottle of beer on the wall.

1 bottle of beer on the wall, 1 bottle of beer.
Take one down, pass it around, no more bottles of beer on the wall!""")
        
    return

def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    
    WEEKS = 6
    total_hours = 0
    
    for i in range(1, WEEKS+1):
        print(f"Week {i}")
        for j in range (1, ia_count+1):
            hours = float(input("\tMarking hours for IA " + str(j) + ": "))
            total_hours = total_hours + hours
            
    return(total_hours)
            
def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """

    value1 = max = min = total = float(input("First values: "))

    total = 0
    
    for i in range(n-1):
        values = float(input("Next value: "))
        if values < min:
            min = values
        if values > max:
            max = values
        total += values
        
    maximum = max
    minimum = min
    total = total + value1
    average = total / n
    
    return(minimum, maximum, total, average)
    