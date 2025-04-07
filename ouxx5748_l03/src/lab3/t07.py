"""
-------------------------------------------------------
Lab 3, Task 7
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-09-26"
-------------------------------------------------------
"""

breakfast = float(input("Enter cost of breakfast: $"))
lunch  = float(input("Enter cost of lunch: $"))
supper = float(input("Enter cost of supper: $"))

total = breakfast + lunch + supper

print("Meal        \tCost")
print(f"Breakfast: \t${breakfast:>6.2f}")
print(f"Lunch:     \t${lunch:>6.2f}")
print(f"Supper:    \t${supper:>6.2f}")
print(f"Total:     \t${total:>6.2f}")
