"""
-------------------------------------------------------
Lab 2, Task 6
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-09-19"
-------------------------------------------------------
"""

principal = float(input("Mortgage principal ($): "))

years = int(input("Number of years: "))
monthly_payments = years * 12

rate = int(input("Yearly interest rate (%): "))
percent_rate = (rate/100)/12

top_equation = percent_rate*(percent_rate+1)**monthly_payments
bottom_equation = (percent_rate+1)**monthly_payments - 1

mortgage = principal * top_equation/bottom_equation

print("The monthly payments are: $", mortgage)
