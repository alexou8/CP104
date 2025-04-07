"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-04"
-------------------------------------------------------
"""

date_reversed = int(input("Enter a date format DDMMYYYY: "))

year = date_reversed % 10000
month = (date_reversed//10000) % 100
day = (date_reversed//10000) // 100

print(f"The reformatted date: {year}/{month}/{day}")
