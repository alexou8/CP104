"""
-------------------------------------------------------
Lab 2, Task 13
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-09-19"
-------------------------------------------------------
"""

mid = float(input("Midterm mark (%): "))
final = float(input("Exam mark (%): "))

MIDTERM = 0.35 
EXAM = 0.65 

midterm_grade = mid * MIDTERM
exam_grade = final * EXAM

final_grade = midterm_grade + exam_grade

print("Final Grade (%):", final_grade)