"""Build 02 - Modifying lists.

Run this file:  python build-02.py
"""

# --- Overwriting elements in a list -----------------------------------------

tech_accessories = ['USB Cable', 'Headphones', 'Mouse Pad', 'Power Bank']
print(tech_accessories)  # Prints the original list before modifications.

tech_accessories[0] = 'TV'  # Changing USB Cable -> TV

print(tech_accessories)  # Prints the new list

print()

# --- Appending elements -----------------------------------------------------

# Starting fresh, so the previous section's change does not carry over.
tech_accessories = ['USB Cable', 'Headphones', 'Mouse Pad', 'Power Bank']

tech_accessories.append("Wireless Charger")

print(tech_accessories)  # Printing out the new list

print()

# --- Inserting elements -----------------------------------------------------

tech_accessories = ['USB Cable', 'Headphones', 'Mouse Pad', 'Power Bank']

tech_accessories.insert(2, "Telephone")  # inserted at index 2, the third position

print(tech_accessories)
