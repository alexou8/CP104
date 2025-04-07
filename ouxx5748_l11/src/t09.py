"""
-------------------------------------------------------
Lab 11, Task 9
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-28"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_char, count_frequency

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
char = input("Enter character to count: ")

matrix = generate_matrix_char(rows, cols)

count = count_frequency(matrix, char)

print(matrix)
print(count)
