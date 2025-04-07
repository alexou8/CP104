"""
-------------------------------------------------------
Lab 2, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-09-19"
-------------------------------------------------------
"""

FREEZE = 32

fahrenheit = int(input("Temperature (F): "))


formula = float((fahrenheit - FREEZE) * 5/9)

print("Temperature (C):", formula)

