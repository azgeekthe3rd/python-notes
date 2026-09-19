"""Build 02 - Using the range() function and simple statistics.

Run this file:  python build-02.py
"""


# --- Applying the range() function ---

for value in range(1,6):
    print(value)

print()


# --- Creating lists with the range() function ---

numbers_list = list(range(1,11))
print(numbers_list)

print()


# --- Building a bigger example ---

numbers = [] # Creating an empty list to store the squared values

print(f"Here is the list before we add any square values: {numbers}") # We display the list before we add any square values

print("\nNow we display the range of numbers from 1 to 10 before we square them:") # Here we display the range of numbers from 1 to 10 before we square them
for number in range(1, 11):
    squared_value = number ** 2 # Here we square the value of each number
    numbers.append(squared_value) # Here we square the value of each number and append it to the list
    print(number) # Here we display the range of numbers from 1 to 10 before we square them

print(f"\nHere is what the list looks after we squared the values and appended them to the list: {numbers}\n") # Displays the squared values in the list

print()


# --- Applying simple statistics to the values in a list. ---

numbers = [42, 32, 53, 12, 84, 64, 23]

print("Here are the stats for the numbers in the list: ")

print(f"\tMax: {max(numbers)}") # The max() function finds the largest number in the list.
print(f"\tMin: {min(numbers)}") # The min() function, finds the smallest number in the list.
print(f"\tSum: {sum(numbers)}") # The sum() function calculates the total of all the numbers in the list.

print()



# --- Applying simple statistics to real data ---

numbers = [12, 45, 67, 23, 89, 34, 56, 78, 90, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 150, 3, 9, 27, 81, 243, 12, 18, 24, 36, 48]

len_numbers = len(numbers) # Finding the number of items in the list

max_numbers = max(numbers) # Finding the maximum value

min_numbers = min(numbers) # Finding the minimum value

sum_numbers = sum(numbers) # Calculating the Sum of values

avg_numbers = sum_numbers / len_numbers # Calculating the average

print(f"Here is all the stats of the numbers: \n\tLength: {len_numbers}\n\tMax: {max_numbers}\n\tMin: {min_numbers}\n\tSum: {sum_numbers}\n\tMean: {avg_numbers}") # Displaying the values with f-string

