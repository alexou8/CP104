"""
-------------------------------------------------------
Assignment 7, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-15"
-------------------------------------------------------
"""
# Imports
from functions import list_indexes, list_positives

values = list_positives()

target = int(input("Enter target value: "))

indexes = list_indexes(values, target)

print(indexes)
