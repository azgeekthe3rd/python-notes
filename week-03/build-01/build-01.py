"""Build 01 - Looping Through Lists.

Run this file:  python build-01.py
"""

### --- Looping through the entire list ---

ninja_moves = ['Punch', 'Kick', 'Flip', 'Block', 'Dash']

for move in ninja_moves: # Iterate through each item in the list
    print(move) 

print()

### --- Applying f-strings in loops ---

names = ['Ali', 'Sara', 'Omar', 'Fatima', 'Hassan']

for name in names: # Iterate through each item in the inventory
    print(f"Hello, {name}, welcome to our society!")