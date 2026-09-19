"""Week 3 - Lab solutions.

Only read this after you have attempted the lab yourself.

There is more than one correct way to write most of these. If yours
produces the right output by a different route, yours is also correct.
"""

# =============================================================================
# Task 1 - Looping through a list
# =============================================================================

numbers = [1, 3, 9, 27]
squares = []

for number in numbers:
    squares.append(number ** 2)

print(f"Here is the initial list: {numbers}")
print(f"Here is the modified list: {squares}")


# =============================================================================
# Task 2 - range() and simple statistics
# =============================================================================

numbers = list(range(1, 6))

max_number = max(numbers)
min_number = min(numbers)
sum_number = sum(numbers)

print(f"Stats:\n\tMax: {max_number}\n\tMin: {min_number}\n\tSum: {sum_number}")


# =============================================================================
# Task 3 - Slicing a list
# =============================================================================

numbers = [1, 4, 5, 9, 29, 43, 53, 34]

print(f"The first three items: {numbers[:3]}")
print(f"The last four items: {numbers[-4:]}")


# =============================================================================
# Task 4 - Copying a list
# =============================================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_copy = numbers[:]

numbers.append(49)
numbers_copy.append(24)

print(f"The original list: {numbers}")
print(f"The copied list:   {numbers_copy}")


# =============================================================================
# Task 5 - Overwriting a tuple
# =============================================================================

my_tuple = (2, 4, 6, 8, 10)
print(f"The original tuple: {my_tuple}")

my_tuple = (2, 9)
print(f"The new tuple:      {my_tuple}")
