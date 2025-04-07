"""
-------------------------------------------------------
Lab 6, Task 14
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-24"
-------------------------------------------------------
"""
# Imports
from functions import ia_hours

ia_count = int(input("Enter number of IAs: "))

total_hours = ia_hours(ia_count)

print(f"{total_hours:.2f}")