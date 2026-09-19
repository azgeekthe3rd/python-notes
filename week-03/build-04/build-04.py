"""Build 04 - Tuples

Run this file:  python build-04.py
"""

# --- What is a Tuple? ---

my_tuple = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
print(my_tuple[0]) # Prints 2.


# --- Tuples cannot be changed ---

my_tuple = (10, 100, 1000, 100000, 1000000)

# Uncomment the line below to see the error for yourself.
# Tuples do not allow item assignment, unlike lists.

# my_tuple[2] = 30

print()

# --- Looping through values in a Tuple ---
my_tuple = (1, 7, 2 ,5)

for number in my_tuple: # Looping through the tuple
    print(number)

print()

# --- The Comma Rule for Single‑Item Tuples ---
with_comma = (50,)
without_comma = (50)

print(with_comma)
print(without_comma)

print()

# --- Writing over a Tuple ---
my_tuple = (15, 20)
print(my_tuple)

my_tuple = (50, 500)
print(my_tuple)