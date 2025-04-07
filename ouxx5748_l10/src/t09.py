"""
-------------------------------------------------------
Lab 10, Task 9
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-24"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_value

fh = open("numbers.txt", "r", encoding="utf-8")

print("file 'numbers.txt' open for reading")

value = int(input("Value to count: "))

count = count_frequency_value(fh, value)

print(f"{value} appears {count} time(s)")
