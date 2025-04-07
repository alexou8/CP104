"""
-------------------------------------------------------
Lab 10, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-23"
-------------------------------------------------------
"""
# Imports
from functions import customer_first

fh = open("customers.txt", "r", encoding="utf-8")
result = customer_first(fh)

print(result)

fh.close()
