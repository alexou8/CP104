"""
-------------------------------------------------------
Lab 8, Task 8
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-07"
-------------------------------------------------------
"""
# Imports
from functions import linear_search

values = []

nums = int(input("Enter number of values: "))

for i in range(0, nums):
    num = int(input("Enter value: "))
    values.append(num)

value = int(input("Enter value to search for: "))

index = linear_search(values, value)

print(index)
