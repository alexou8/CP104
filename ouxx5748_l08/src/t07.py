"""
-------------------------------------------------------
Lab 8, Task 7
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-07"
-------------------------------------------------------
"""
# Imports
from functions import list_categorize
from functions import generate_integer_list

n = int(input("Enter number of values: "))
low = int(input("Enter lowest number of values: "))
high = int(input("Enter highest number of values: "))

values = generate_integer_list(n, low, high)

negatives, positives, zeroes, evens, odds = list_categorize(values)

print(f"({negatives}, {positives}, {zeroes}, {evens}, {odds})")
