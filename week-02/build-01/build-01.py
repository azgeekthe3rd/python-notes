"""Build 01 - Introduction to lists.

Run this file:  python build-01.py
"""

# --- Building your first list -----------------------------------------------

grocery_list = ['Milk', 'Butter', 'Ketchup', 'Eggs', 'Lettuce']
print(grocery_list)

print()

# --- Returning specific elements --------------------------------------------

print(grocery_list[0])

print(f"Please don't forget the {grocery_list[0].upper()}!")

print(grocery_list[3])
print(grocery_list[4])

print()

# --- Printing the final item ------------------------------------------------

fruit_basket = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
print(fruit_basket[-1])

print()

# --- Going out of range -----------------------------------------------------

# Uncomment the line below to see the IndexError for yourself.
# The list only has 5 items, so index 6 does not exist.

# print(fruit_basket[6])
