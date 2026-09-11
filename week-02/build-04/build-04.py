"""Build 04 - Organizing lists.

Run this file:  python build-04.py
"""

# --- Sorting permanently with sort() ----------------------------------------

travel_essentials = ['Passport', 'Boarding Pass', 'Travel Pillow',
                     'Water Bottle', 'Phone Charger']

travel_essentials.sort()  # Sorting the list into alphabetical order

print(travel_essentials)  # Printing the list

print()

# --- Sorting is not purely alphabetical -------------------------------------

# Capitals sort before lowercase letters, because Python compares
# character codes rather than letters.
print(sorted(['banana', 'Apple', 'cherry']))

print()

# --- Sorting in reverse -----------------------------------------------------

travel_essentials = ['Passport', 'Boarding Pass', 'Travel Pillow',
                     'Water Bottle', 'Phone Charger']

travel_essentials.sort(reverse=True)  # Reverse-alphabetical order

print(travel_essentials)  # Printing the new list

print()

# --- Sorting temporarily with sorted() --------------------------------------

travel_essentials = ['Water Bottle', 'Travel Pillow', 'Phone Charger',
                     'Passport', 'Boarding Pass']

print("Here is the original list: ")
print(travel_essentials)

print("Here is the sorted list: ")
print(sorted(travel_essentials))

print("Here is the original list again: ")
print(travel_essentials)

print()

# --- Reversing the current order --------------------------------------------

travel_essentials = ['Water Bottle', 'Travel Pillow', 'Phone Charger',
                     'Passport', 'Boarding Pass']

travel_essentials.reverse()  # This reverses the list

print(travel_essentials)     # This shows the reversed list

print()

# --- Finding the length -----------------------------------------------------

travel_essentials = ['Water Bottle', 'Travel Pillow', 'Phone Charger',
                     'Passport', 'Boarding Pass']

print(len(travel_essentials))
