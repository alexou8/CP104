"""
-------------------------------------------------------
Lab 10, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-24"
-------------------------------------------------------
"""
# Imports
from functions import customer_append

fh = open("customers.txt", "w", encoding="utf-8")
fields = ['35612', 'David', 'Brown', 237.56, '2008-10-10']

customer_append(fh, fields)

fh.close()
