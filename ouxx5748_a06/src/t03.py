"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-08"
-------------------------------------------------------
"""
# Imports
from functions import interest_table

principal = float(input("Enter value of the loan: "))
rate = float(input("Enter yearly interest rate in %: "))
payment = float(input("Enter monthly payment: "))

interest_table(principal, rate, payment)
