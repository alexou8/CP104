"""
-------------------------------------------------------
Lab 9, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-15"
-------------------------------------------------------
"""
# Imports
from functions import url_categorize

url = input("Enter url: ")

url_type = url_categorize(url)

print(url_type)
