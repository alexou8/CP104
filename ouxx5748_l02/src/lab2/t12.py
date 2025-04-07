"""
-------------------------------------------------------
Lab 2, Task 12
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-09-19"
-------------------------------------------------------
"""

seconds = int(input("Enter number of seconds: "))

DAY = 60 * 60 * 24
HOUR = 60 * 60
MIN = 60

days = seconds // DAY
hours = (seconds - (days * DAY)) // HOUR
mins = (seconds - (days * DAY) - (hours * HOUR)) // MIN
secs = seconds % 60

print("Days:", days, "Hours:", hours, "Minutes:", mins, "Seconds:", secs)