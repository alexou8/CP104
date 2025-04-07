"""
-------------------------------------------------------
Lab 11, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-28"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_char, print_matrix_char

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = generate_matrix_char(rows, cols)

print_matrix_char(matrix)
