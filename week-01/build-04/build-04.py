"""Build 04 - Numbers and maths.

Run this file:  python build-04.py
"""

# --- The operators ----------------------------------------------------------

print(7 + 3)
print(7 - 3)
print(7 * 3)
print(7 / 3)
print(7 // 3)
print(7 % 3)
print(7 ** 3)

print()

# --- Division always gives a float ------------------------------------------

print(10 / 2)
print(7 // 2)

# --- Remainder: 0 means it divides evenly -----------------------------------

print(10 % 2)
print(11 % 2)

print()

# --- Floats are not exact ---------------------------------------------------

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

print()

# --- Large numbers ----------------------------------------------------------

population = 57_128_461_853_718
print(population)

print()

# --- Several variables at once ----------------------------------------------

x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

print()

# --- Constants --------------------------------------------------------------

FREEZING_POINT_C = 0
BOILING_POINT_C = 100
SECONDS_IN_A_DAY = 86_400

print(f"Water freezes at {FREEZING_POINT_C} degrees Celsius")
print(f"Water boils at {BOILING_POINT_C} degrees Celsius")
print(f"There are {SECONDS_IN_A_DAY} seconds in a day")
