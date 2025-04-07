"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-04"
-------------------------------------------------------
"""

sales = float(input("Enter the total sales: $"))

TAX = 18.50
total_tax = sales * (TAX/100)

print(f"""
Projected Tax Report
--------------------------
Total Sales:   $ {sales:,.2f}
Annual tax:    % 18.50
--------------------------
Tax:           $ {total_tax:,.2f}""")