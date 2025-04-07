"""
-------------------------------------------------------
Lab 8, Task 14
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-07"
-------------------------------------------------------
"""
# Imports
from functions import intersection

source1 = []
source2 = []

nums = int(input("Enter number of values in source one: "))

for i in range(0, nums):
    num = int(input("Enter value: "))
    source1.append(num)

nums = int(input("Enter number of values in source two: "))

for i in range(0, nums):
    num = int(input("Enter value: "))
    source2.append(num)

target = intersection(source1, source2)

print(target)
