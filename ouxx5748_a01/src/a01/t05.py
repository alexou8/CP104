"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-09-27"
-------------------------------------------------------
"""

P = float(input("Principal: $"))
R = float(input("Interest (decimal): "))
T = int(input("Number of years: "))
N = int(input("Number of times interest compounded per year: "))

formula = P*(1 + (R/N))**(N * T)

print("Balance: $", formula)