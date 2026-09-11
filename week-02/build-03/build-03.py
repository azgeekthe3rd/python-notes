"""Build 03 - Removing elements from a list.

Run this file:  python build-03.py
"""

# --- Removing elements using del --------------------------------------------

study_essentials = ['Notebook', 'Pen', 'Sticky Notes', 'Calculator']

print(study_essentials)  # Printing the original list

del study_essentials[0]  # We delete the first element

print(study_essentials)  # Printing out the modified list

print()

# --- Removing with the pop() method -----------------------------------------

study_essentials = ['Notebook', 'Pen', 'Sticky Notes', 'Calculator']

last_item = study_essentials.pop()  # Removes the last item and returns it

print(last_item)         # Shows the item that was popped
print(study_essentials)  # Shows the updated list

print()

# --- Using the popped item with a string method -----------------------------

study_essentials = ['Notebook', 'Pen', 'Sticky Notes', 'Calculator']

last_item = study_essentials.pop()  # Takes the final element out of the list

print(f"I forgot to bring my {last_item.lower()} for the exam.")

print()

# --- Removing an item by name with remove() ---------------------------------

study_essentials = ['Notebook', 'Pen', 'Sticky Notes', 'Calculator']

print(study_essentials)  # Printing out the original list

study_essentials.remove('Pen')  # Naming the element we want removed

print(study_essentials)  # Printing the new list
