"""
-------------------------------------------------------
Lab 9, Task 10
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-11-15"
-------------------------------------------------------
"""
# Imports
from functions import text_analyze

txt = input("Enter text: ")

uppr, lowr, dgts, whtspc = text_analyze(txt)

print(f"({uppr}, {lowr}, {dgts}, {whtspc})")
