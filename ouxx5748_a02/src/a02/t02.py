"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-04"
-------------------------------------------------------
"""

integer = int(input("Enter a positive digit number: "))

num = integer
product = 1
 
while (num!=0):
    product = product * (num%10)
    num = num // 10
 
    
print(f"The product of the digits of {integer} is {product}")

