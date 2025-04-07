"""
-------------------------------------------------------
Lab 9, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-15"
-------------------------------------------------------
"""
# Imports
from functions import validate_code

product_code = input("Enter product code: ")

category, digits, qualifiers = validate_code(product_code)

print(f"({category}, {digits}, {qualifiers})")
