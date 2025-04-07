"""
-------------------------------------------------------
Lab 9, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-15"
-------------------------------------------------------
"""
# Imports
from functions import parse_code

product_code = input("Enter product code: ")

pc, pi, pq = parse_code(product_code)

print(f"('{pc}', '{pi}', '{pq}')")
