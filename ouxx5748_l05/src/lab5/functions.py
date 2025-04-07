"""
-------------------------------------------------------
Lab 5, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    
    check1 = target - v1
    check2 = target - v2
    
    checked = v1
    
    if abs(check1) < abs(check2) or abs(check1) == abs(check2):
        checked = v1
    else:
        checked = v2
    
    return checked
    
def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    
    check = True
    
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        check = True
    else:
        check = False
        
    return check
        
def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - name of: quadrant, axis, or origin of coordinate x, y (str)
    -------------------------------------------------------
    """
    
    quad = "Q4"
    
    if x < 0 and y < 0:
        quad = "Quadrant 3"
    elif x > 0 and y > 0:
        quad = "Quadrant 1"
    elif (x > 0 and y > 0) or (x < 0 and y > 0):
        quad = "Quadrant 2"
    elif x == 0 and y == 0:
        quad = "Origin"
    elif x == 0 and y != 0:
        quad = "Y-Axis"
    elif x != 0 and y == 0:
        quad = "X-Axis"
    else:
        quad = "Quadrant 4"
        
    return quad
    
def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    
    MIN_YEAR = 5
    MIN_SALARY = 30000
    
    YEARS = int(input("Years employed: "))
    
    check = True
    
    if YEARS >= MIN_YEAR:
        SALARY = int(input("Annual salary: "))
        if SALARY < MIN_SALARY:
            check = False
        elif SALARY >= MIN_SALARY:
            check = True
    elif YEARS < MIN_YEAR:
        check = False
    
    return check

def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    
    food = input("Order B - burger or W - wings: ")
    
    BURGER = 6.00
    WINGS = 8.00
    FRIES = 1.50
    SALAD = 2.00
    
    total = 0
    
    if food == "B":
        total = total + BURGER
        combo_option = input("Make it a combo? (Y/N): ")
        if combo_option == "Y":
            combo = input("Add F - fries or S - salad: ")
            if combo == "F":
                total = total + FRIES
            elif combo == "S":
                total = total + SALAD
        else:
            total = total
    if food == "W":
        total = total + WINGS
        combo_option = input("Make it a combo? (Y/N): ")
        if combo_option == "Y":
            combo = input("Add F - fries or S - salad: ")
            if combo == "F":
                total = total + FRIES
            elif combo == "S":
                total = total + SALAD
        else:
            total = total
    
    return total
    
    