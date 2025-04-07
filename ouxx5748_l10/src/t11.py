"""
-------------------------------------------------------
Lab 10, Task 11
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-24"
-------------------------------------------------------
"""
# Imports
from functions import find_longest

fh = open("words.txt", "r", encoding="utf-8")

word = find_longest(fh)

print("file 'words.txt' open for reading")
print(f"'{word}' is the last longest word")
