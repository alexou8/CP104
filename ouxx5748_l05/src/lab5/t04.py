"""
-------------------------------------------------------
Lab 5, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
from functions import closest

target = float(input("Enter target number: "))
v1 = float(input("Enter number 1: "))
v2 = float(input("Enter number 2: "))

result = closest(target, v1, v2)

print(f"{result:.1f}")
