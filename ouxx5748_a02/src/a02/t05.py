"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Zi Feng (Alex) Ou
ID:          169025748
Email:     ouxx5748@mylaurier.ca
__updated__ = "2022-10-04"
-------------------------------------------------------
"""

f_length = float(input("Foundation length (m): "))
f_width = float(input("Foundation width (m): "))
f_height = float(input("Foundation height (m): "))
w_height = float(input("Wall height (m): "))
c_cost = float(input("Cost of concrete ($/m^3): "))
b_cost = float(input("Cost of brick ($/m^2): "))

concrete = f_length * f_width * f_height
concrete_cost = concrete * c_cost

bricks = (2 * (f_length*w_height)) + (2 * (f_width*w_height))
bricks_cost = bricks * b_cost

total_cost = concrete_cost + bricks_cost

print(f"""
Concrete needed for foundation (m^3): {concrete:.2f}
Cost of concrete: ${concrete_cost:,.2f}
Bricks needed for walls (m^2): {bricks:.2f}
Costs of bricks: ${bricks_cost:,.2f}
Total cost: ${total_cost:,.2f}
""")