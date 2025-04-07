"""
-------------------------------------------------------
Assignment 5, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports
from functions import range_total

start = int(input("Enter start value: "))
increment = int(input("Enter increment value: "))
count = int(input("Enter number of values: "))

total = range_total(start, increment, count)

print(total)