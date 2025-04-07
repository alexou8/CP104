"""
-------------------------------------------------------
Lab 7, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports

def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    
    years = 0
    
    while current < target:
        current = current * (1 + rate/100)
        years = years + 1
    
    return years
    
def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    
    first_num = float(input("First positive value: "))
    
    
    count = 1  
    minimum = first_num
    maximum = first_num
    total = first_num
    next_num = 0
    
    
    while next_num >= 0:
        next_num = float(input("Next positive value: "))
        if next_num < 0:
            break
        if next_num < minimum:
            minimum = next_num
        if next_num > maximum:
            maximum = next_num
        total = total + next_num
        count = count + 1
    
    average = total / count
    
    return(minimum, maximum, total, average)

def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    
    count = 1
    b_total = 0
    l_total = 0
    s_total = 0
    
    check = 'Y'
    
    while check == 'Y':
        print(f"For Day {count}")
        breakfast = float(input("How much was breakfast? "))
        b_total = b_total + breakfast
        d_total = breakfast
        lunch = float(input("How much was lunch? "))
        l_total = l_total + lunch
        d_total = d_total + lunch
        supper = float(input("How much was supper? "))
        s_total = s_total + supper
        d_total = d_total + supper
        print(f"Your total for the day was ${d_total}")
        check = input("Were you away another day (Y/N)? ")
        count = count + 1
        
    a_total = b_total + l_total + s_total
    
    return(b_total, l_total, s_total, a_total)
        
def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    
    check = 1
    status = 'Balanced'
    
    first_expense = float(input("Enter an expense (0 to quit): $"))
    expenses = first_expense
    balance = available - first_expense
    
    if first_expense == 0:
        check = 0
    
    while check != 0:
        expense = float(input("Enter another expense (0 to quit): $"))
        expenses = expenses + expense
        balance = balance - expense
        check = expense
    
    if balance < 0:
        status = 'Deficit'
    if balance > 0:
        status = 'Surplus'
    
    return(expenses, balance, status)

def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    
    check = 0
    
    while check == 0:
        value = int(input(f"Enter a value between {low} and high {high}: "))
        if value < low:
            print("Value entered is too low")
        if value > high:
            print("Value entered is too high")
        if value >= low and value <= high:
            check = 1
            break
    
    return value
        