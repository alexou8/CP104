"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-04"
-------------------------------------------------------
"""

cakes = int(input("Number of pieces of cakes: "))
people = int(input("Number of party-goers: "))

person_cake = cakes // people
remainder_cake = cakes % people

print(f"""Each party-goer receives {person_cake} pieces of cake
Pieces of cake that won't be distributed: {remainder_cake}""")