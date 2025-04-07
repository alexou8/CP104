"""
-------------------------------------------------------
Assignment 9, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-12-02"
-------------------------------------------------------
"""
# Imports
from functions import file_integers

fh = open("numbers.txt", "r", encoding="utf-8")

numbers = file_integers(fh)

print(numbers)

fh.close()
