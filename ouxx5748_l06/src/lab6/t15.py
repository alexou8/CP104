"""
-------------------------------------------------------
Lab 6, Task 15
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-24"
-------------------------------------------------------
"""
# Imports
from functions import statistics

n = int(input("Enter number of values: "))

minimum, maximum, total, average = statistics(n)

print(f"({minimum:.2f}, {maximum:.2f}, {total:.2f}, {average:.2f})")