"""
-------------------------------------------------------
Assignment 8, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-25"
-------------------------------------------------------
"""
# Imports
from functions import is_valid_isbn

isbn = input("Enter ISBN: ")

valid = is_valid_isbn(isbn)

print(valid)
