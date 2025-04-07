"""
-------------------------------------------------------
Lab 10, Task 14
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-25"
-------------------------------------------------------
"""
# Imports
from functions import file_copy_n

fh_1 = open("words.txt", "r", encoding="utf-8")
fh_2 = open("new_words.txt", "w", encoding="utf-8")

print("Copying 'words.txt' to 'new_words.txt'")
n = int(input("Number of lines to copy: "))

file_copy_n(fh_1, fh_2, n)

fh_1.close()
fh_2.close()
