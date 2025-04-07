"""
-------------------------------------------------------
Assignment 9, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:           169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-12-05"
-------------------------------------------------------
"""
# Imports
from functions import student_info

students = open("students.txt", "r", encoding="utf-8")

l_id, h_id, avg = student_info(students)

print(f"('{l_id}', '{h_id}', {avg})")

students.close()
