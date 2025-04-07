"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-24"
-------------------------------------------------------
"""
# Imports
from functions import product_largest

v1 = float(input("Enter a number: "))
v2 = float(input("Enter a number: "))
v3 = float(input("Enter a number: "))

product = product_largest(v1, v2, v3)

print(f"{product:.0f}")
