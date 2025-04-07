"""
-------------------------------------------------------
Lab 4, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""
# Imports
from functions import right_triangle

a = float(input("Enter adjacent length of triangle: "))
o = float(input("Enter opposite length of triangle: "))

calc = right_triangle(a, o)

print(calc)