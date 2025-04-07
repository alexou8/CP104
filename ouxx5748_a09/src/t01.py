"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-29"
-------------------------------------------------------
"""
# Imports
from functions import file_head

file = "functions.py"

fh = open(file, "r", encoding="utf-8")

print(f"Reading file from: {file}")

file_head(fh, 5)

fh.close()
