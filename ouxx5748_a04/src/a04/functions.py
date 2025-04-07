"""
-------------------------------------------------------
Assignment 4, Functions
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-24"
-------------------------------------------------------
"""
# Imports

def day_of_week(day_number):
    """
    -------------------------------------------------------
    Takes an integer parameter and returns a string representing 
    the corresponding day of the week.
    i.e. 1 = "Monday", 2 = "Tuesday", etc.
    Use: day_of_week = day_of_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - day of the week represented by the integer (int)
    Returns:
        day - Day of the week in a string (str)
    ------------------------------------------------------
    """
    
    day = ''
    
    if day_number == 1:
        day = 'Monday'
    elif day_number == 2:
        day = 'Tuesday'
    elif day_number == 3:
        day = 'Wednesday' 
    elif day_number == 4:
        day = 'Thursday' 
    elif day_number == 5:
        day = 'Friday'
    elif day_number == 6:
        day = 'Saturday'
    elif day_number == 7:
        day = 'Sunday'
    else:
        day = 'Error'
    
    return day       

def pollution_level(aqi):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level = pollution_level(aqi)
    -------------------------------------------------------
    Parameters:
        aqi - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    
    level = ''
    
    if aqi < 0:
        level = 'Error';
    elif aqi <= 50:
        level = 'Good'
    elif aqi <= 100:
        level = 'Moderate'
    elif aqi <= 150:
        level = 'Unhealthy for Sensitive Groups'
    elif aqi <= 200:
        level = 'Unhealthy'
    elif aqi <= 300:
        level = "Very Unhealthy"
    elif aqi > 300:
        level = 'Hazardous'
        
    return level

def product_largest(v1, v2, v3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    v1, v2, and v3.
    Use: product = product_largest(v1, v2, v3)
    -------------------------------------------------------
    Parameters:
        v1 - a number (float)
        v2 - a number (float)
        v3 - a number (float)
    Returns:
        product - the product of the two largest values of
            v1, v2, and v3 (float)
    ------------------------------------------------------
    """
    
    max1 = 0
    max2 = 0
    
    if v1 >= v2 and v1 >= v3:
        max1 = v1
        if v2 >= v3:
            max2 = v2
        else:
            max2 = v3
    if v2 >= v1 and v2 >= v3:
        max1 = v2
        if v1 >= v3:
            max2 = v1
        else:
            max2 = v3
    if v3 >= v1 and v3 >= v2:
        max1 = v3
        if v1 >= v2:
            max2 = v1
        else:
            max2 = v2
    
    product = max1 * max2
    
    return product
    
def rgb_mix(rgb1, rgb2):
    """
    -------------------------------------------------------
    Determines the secondary colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: colour = rgb_mix(rgb1, rgb2)
    -------------------------------------------------------
    Parameters:
        rgb1 - a primary RGB colour (str)
        rgb2 - a primary RGB colour (str)
    Returns:
        colour - a secondary RGB colour (str)
    -------------------------------------------------------
    """
    
    colour = ''
    
    if rgb1 == 'red' and rgb2 == 'red':
        colour = 'red'
    elif rgb1 == 'green' and rgb2 == 'green':
        colour = 'green'
    elif rgb1 == 'blue' and rgb2 == 'blue':
        colour = 'blue'
    elif rgb1 == 'red' and rgb2 == 'green' or rgb1 == 'green' and rgb2 == 'red':
        colour = 'yellow'
    elif rgb1 == 'red' and rgb2 == 'blue' or rgb1 == 'blue' and rgb2 == 'red':
        colour = 'fuchsia'
    elif rgb1 == 'red' and rgb2 == 'green' or rgb1 == 'green' and rgb2 == 'red':
        colour = 'yellow'
    elif rgb1 == 'green' and rgb2 == 'blue' or rgb1 == 'blue' and rgb2 == 'green':
        colour = 'aqua'
    else:
        colour = 'Error'
    
    return colour

def yee_ha(number):
    """
    -------------------------------------------------------
    Takes in a number and determines if it is evenly divisible
    by 3, 7, or both.
    Returns "Yee" if evenly divisible by 3
    Returns "Ha" if evenly divisible by 7
    Returns "Yee Ha" if evenly divisible by both
    Returns "Nada" if the number is none of the above
    Use: yeeha_check = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number - a integer to check if divisible (int)
    Returns:
        yeeha_check - a string depending on divisibility (str)
    -------------------------------------------------------
    """
    
    yeeha_check = ''
    
    if number%3 == 0:
        yeeha_check = 'Yee'
    if number%7 == 0:
        yeeha_check = 'Ha'
    if number%3 == 0 and number%7 == 0:
        yeeha_check = 'Yee Ha'
    else:
        yeeha_check = 'Nada'
    
    return yeeha_check
    