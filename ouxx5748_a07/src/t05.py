"""
-------------------------------------------------------
Assignment 7, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-15"
-------------------------------------------------------
"""
# Imports
from functions import is_sorted, list_positives

values = list_positives()

in_order, index = is_sorted(values)

print(f"{in_order}, {index}")
