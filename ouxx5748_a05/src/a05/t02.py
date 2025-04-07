"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports
from functions import calories_burned

calories_min = float(input("Enter calories burned per minute: "))
mins = int(input("Enter total minutes running: "))

total_burned = calories_burned(calories_min, mins)