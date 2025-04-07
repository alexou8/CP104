"""
-------------------------------------------------------
Lab 3, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-09-26"
-------------------------------------------------------
"""

num = float(input("Enter number: "))
percent = float(input("Enter percent: "))

discount = num * (percent/100)

print(f"A {percent:.1f} percent discount on {num:.1f} is {discount:.1f}")