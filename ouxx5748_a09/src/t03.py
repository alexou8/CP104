"""
-------------------------------------------------------
Assignment 9, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-29"
-------------------------------------------------------
"""
# Imports
from functions import file_stats

file = "functions.py"

fh = open(file, "r", encoding="utf-8")

ucount, lcount, dcount, wcount = file_stats(fh)

print(print(f"Reading file from: {file}"))
print(f"({ucount}, {lcount}, {dcount}, {wcount})")

fh.close()
