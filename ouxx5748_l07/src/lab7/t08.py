"""
-------------------------------------------------------
Lab 7, Task 8
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports
from functions import budget

available = float(input("Enter available funds: "))

expenses, balance, status = budget(available)

print(f"({expenses:.2f}, {balance:.2f}, {status})")