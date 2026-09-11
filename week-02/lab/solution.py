"""Week 2 - Lab solutions.

Only read this after you have attempted the lab yourself.

There is more than one correct way to write most of these. If yours
produces the right output by a different route, yours is also correct.
"""

# =============================================================================
# Task 1 - Indexing + .upper() + f‑string
# =============================================================================

fruit_basket = ['Apple', 'Banana', 'Cherry', 'Orange', 'Grapes']

print(f"The first fruit in the basket is {fruit_basket[0].upper()}")


# =============================================================================
# Task 2 - .append() + .insert()
# =============================================================================

animals = ['Cat', 'Dog', 'Rabbit', 'Horse', 'Elephant']

animals.append("Giraffe")  # Add Giraffe to the end of the list

animals.insert(3, "Panda")  # Insert Panda at index 3

print(animals)  # Should print ['Cat', 'Dog', 'Rabbit', 'Panda', 'Horse', 'Elephant', 'Giraffe']

# =============================================================================
# Task 3 - del, .pop(), .remove()
# =============================================================================

colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']

print(f"The original colors are: {colors}")  # Should print ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
del colors[3]  # Remove the color at index 3

second_color = colors.pop(1)  # Remove the color at index 1

colors.remove("Green")

print(f"The remaining colors are: {colors}")  # Should print ['Red', 'Purple'] after the above operations

print(f"The second color that was popped is: {second_color}")  # Should print 'Blue'
# =============================================================================
# Task 4 - .sort(), sort(reverse=True), sorted()
# =============================================================================

countries = ['Japan', 'Canada', 'Brazil', 'France', 'Egypt']

print(sorted(countries))  # Should print ['Brazil', 'Canada', 'Egypt', 'France', 'Japan']

countries.sort()  # Sorts the list in ascending order

print(countries)  # Should print ['Brazil', 'Canada', 'Egypt', 'France', 'Japan']

countries.sort(reverse=True)  # Sorts the list in descending order

print(countries)  # Should print ['Japan', 'France', 'Egypt', 'Canada', 'Brazil']
# =============================================================================
# Task 5 - .reverse() + len()
# =============================================================================

drinks = ['Water', 'Juice', 'Tea', 'Coffee', 'Milk']

drinks.reverse()  # Reverses the order of the list

print(drinks)  # Prints the reversed list

print(len(drinks)) # Prints the number of items in the list