"""
-------------------------------------------------------
Lab 5, Task 11
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
from functions import quadrant

x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

location = quadrant(x, y)

print(location)