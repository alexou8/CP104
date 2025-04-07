"""
-------------------------------------------------------
Lab 11, Task 13
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-28"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_num, matrix_scalar_multiply

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
low = int(input("Enter low value: "))
high = int(input("Enter high value: "))
value_type = input("Enter value type: ")
num = int(input("Enter number to multiply: "))

matrix = generate_matrix_num(rows, cols, low, high, value_type)

print(matrix)

matrix_scalar_multiply(matrix, num)
