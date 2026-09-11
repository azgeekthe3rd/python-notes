"""Build 05 - Comments and putting it together.

Run this file:  python build-05.py
"""

# --- Comments ---------------------------------------------------------------

# This line does nothing at all
print("This line runs")

TAX_RATE = 0.20    # UK standard VAT rate
print(TAX_RATE)

print()

# --- Commenting out code ----------------------------------------------------

print("This runs")
# print("This does not")
print("This runs too")

print()

# --- Putting the week together ----------------------------------------------

# A simple greeting program
# Week 1 - variables, strings, f-strings and maths

# Constants
GREETING = "Hello"
EXCLAMATION = "!"

# User details, with stray whitespace to clean up
first_name = "  john  "
last_name = "  DOE  "
birth_year = 2005
current_year = 2026

# Clean the input and build a full name
first_name = first_name.strip().title()
last_name = last_name.strip().title()
full_name = f"{first_name} {last_name}"

# Work out the age
age = current_year - birth_year

# Output
print(f"{GREETING}, {full_name}{EXCLAMATION}")
print(f"You are {age} years old.")
print(f"Your name is {len(full_name)} characters long.")
