"""
-------------------------------------------------------
Lab 8, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-07"
-------------------------------------------------------
"""
# Imports
from functions import get_lotto_numbers

n = int(input("Enter number of lottery numbers: "))
low = int(input("Enter lowest value of lottery numbers: "))
high = int(input("Enter highest value of lottery numbers: "))

numbers = get_lotto_numbers(n, low, high)

print(numbers)
