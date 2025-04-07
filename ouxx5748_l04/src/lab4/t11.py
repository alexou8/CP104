"""
-------------------------------------------------------
Lab 4, Task 11
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""
# Imports
from functions import slope

x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

coords_slope = slope(x1, y1, x2, y2)

print(coords_slope)