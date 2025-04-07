"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
from functions import date_extract

date_number = int(input("Enter a date in the format MMDDYYYY: "))

year, month, day = date_extract(date_number)

print(f"The reformatted date: {year}/{month}/{day}")