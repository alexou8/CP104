"""
-------------------------------------------------------
Lab 7, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports
from functions import positive_statistics

minimum, maximum, total, average = positive_statistics()

print(f"({minimum:.2f}, {maximum:.2f}, {total:.2f}, {average:.2f})")