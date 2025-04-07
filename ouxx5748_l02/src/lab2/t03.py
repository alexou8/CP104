"""
-------------------------------------------------------
Lab 2, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-09-19"
-------------------------------------------------------
"""

large_dogs = int(input("Number of large dogs groomed: "))
small_dogs = int(input("Number of small dogs groomed: "))

LARGE = 75
SMALL = 50

large_cost = large_dogs * LARGE
small_cost = small_dogs * SMALL

total = large_cost + small_cost

print("Total earned for the day: $", total)
