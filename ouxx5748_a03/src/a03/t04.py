"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
from functions import multiply_fractions

num1 = int(input("Numerator 1: "))
denom1 = int(input("Denominator 1: "))
num2 = int(input("Numerator 2: "))
denom2 = int(input("Denominator 2: "))

numerator, denominator, product = multiply_fractions(num1, denom1, num2, denom2)

print(f"Result: {numerator}/{denominator} = {product:.3f}")