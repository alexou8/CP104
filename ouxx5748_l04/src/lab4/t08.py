"""
-------------------------------------------------------
Lab 4, Task 8
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-03"
-------------------------------------------------------
"""
# Imports
from functions import computer_costs

costs = float(input("Enter cost per computer: "))
amount = int(input("Enter number of computers: "))
commission = float(input("Enter amount of commission: "))

total_one, total_two = computer_costs(costs, amount, commission)

print(f"({total_one:.2f}, {total_two:.2f})")