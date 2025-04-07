"""
-------------------------------------------------------
Lab 7, Task 3
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-31"
-------------------------------------------------------
"""
# Imports
from functions import population_growth

target = int(input("Enter target population: "))
current = int(input("Enter current population: "))
rate = float(input("Enter rate of population increase: "))

years = population_growth(target, current, rate)

print(years)