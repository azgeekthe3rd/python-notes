"""Build 03 - Slicing and copying lists.

Run this file:  python build-03.py
"""

# --- Slicing a list ---

ice_cream = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Cookies and Cream", "Caramel Swirl", "Pistachio", "Mango", "Coffee"]

print(ice_cream[0:3])

print()

# --- Further examples ---


mythical_creatures = ["Dragon", "Phoenix", "Unicorn", "Griffin", "Mermaid", "Hydra", "Centaur", "Minotaur", "Basilisk"]

print(f"Printing the first 4 items in the list: {mythical_creatures[:4]}")

print(f"Printing the last 4 items in the list: {mythical_creatures[-4:]}")

print()



# --- Copying a list ---

ice_cream = ["Vanilla", "Chocolate", "Strawberry", "Mint"]

copy_ice_cream = ice_cream[:]   # this makes a real copy of the original list

print(copy_ice_cream)

print()

# --- Appending values to separate lists ---

ice_cream = ["Vanilla", "Chocolate", "Strawberry", "Mint"]

copy_ice_cream = ice_cream[:]

ice_cream.append("Oreo")

copy_ice_cream.append("Toffee")

print(ice_cream)
print(copy_ice_cream)