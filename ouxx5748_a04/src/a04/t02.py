"""
-------------------------------------------------------
Assignment 4, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-24"
-------------------------------------------------------
"""
# Imports
from functions import pollution_level

aqi = int(input("Enter level of AQI: "))

level = pollution_level(aqi)

print(level)