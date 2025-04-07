"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
from functions import feet_to_acres

square_footage = float(input("Square footage: "))

acres = feet_to_acres(square_footage)

print(f"{acres:.2f} acres is equivalent to {square_footage:,.2f} square feet")