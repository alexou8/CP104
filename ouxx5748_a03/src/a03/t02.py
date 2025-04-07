"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-18"
-------------------------------------------------------
"""
# Imports
from functions import mow_lawn

width = float(input("Width (m): "))
length = float(input("Length (m): "))
speed = float(input("Speed (m^2/minute): "))

time = mow_lawn(width, length, speed)

print(f"Mowing the lawn takes {time:.0f} minutes")