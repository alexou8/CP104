"""
-------------------------------------------------------
Lab 11, Task 6
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-28"
-------------------------------------------------------
"""
from functions import generate_matrix_num, matrix_stats

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
low = int(input("Enter low value: "))
high = int(input("Enter high value: "))
value_type = input("Enter value type: ")

matrix = generate_matrix_num(rows, cols, low, high, value_type)

smallest, largest, total, average = matrix_stats(matrix)

print(matrix)
print(f"({smallest}, {largest}, {total}, {average})")
