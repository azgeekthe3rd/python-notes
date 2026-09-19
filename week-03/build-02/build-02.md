# Build 02 — Using the `range()` function and simple statistics

## Applying the `range()` function:
As we explained in `build-01`, if we want to print every single item in a list, we can simply use loops to go through the entire list and print each item separately. If you're having trouble understanding what this means, I suggest going back and reading that section so you don’t miss anything important. That being said, if we want to print numbers from a range separately, we can use the `range()` function. Here is an example of printing the values from the range 1–5:

```python
for value in range(1,6):
    print(value)
```

The output then becomes:

```bash
$ python3 main.py
1
2
3
4
5
```

## Creating lists with the `range()` function
Now if we wanted to do the opposite, creating new lists consisting of numbers with chosen ranges we could simply do the following:

```python
numbers_list = list(range(1,11))
print(numbers_list)
```

The output for the following code:

```bash
$ python3 main.py
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```


Now lets say you wanted to apply this on a slightly larger scale and use f-string along with it simulating how a project of yours would look you could do the following:

```python
numbers = [] # Creating an empty list to store the squared values

print(f"Here is the list before we add any square values: {numbers}") # We display the list before we add any square values

print("\nNow we display the range of numbers from 1 to 10 before we square them:") # Here we display the range of numbers from 1 to 10 before we square them
for number in range(1, 11):
    squared_value = number ** 2 # Here we square the value of each number
    numbers.append(squared_value) # Here we square the value of each number and append it to the list
    print(number) # Here we display the range of numbers from 1 to 10 before we square them

print(f"\nHere is what the list looks after we squared the values and appended them to the list: {numbers}\n") # Displays the squared values in the list
```
The output we get:
```bash
$ python3 main.py
Here is the list before we add any square values: []

Now we display the range of numbers from 1 to 10 before we square them:
1
2
3
4
5
6
7
8
9
10

Here is what the list looks after we squared those values and appended them to the list: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```


## Applying simple statistics to the values in a list.
We can now combine everything we’ve learned to apply simple statistics. For example, we can find the length of a list, identify the maximum or minimum value, or calculate the sum of all the numbers. Here is an example:

```python
numbers = [42, 32, 53, 12, 84, 64, 23]

print("Here are the stats for the numbers in the list: ")

print(f"\tMax: {max(numbers)}") # The max() function finds the largest number in the list.
print(f"\tMin: {min(numbers)}") # The min() function, finds the smallest number in the list.
print(f"\tSum: {sum(numbers)}") # The sum() function calculates the total of all the numbers in the list.
```

The output:

```bash
$ python3 main.py
Here are the stats for the numbers in the list: 
        Max: 84
        Min: 12
        Sum: 310
```


## Applying simple statistics to real data
Now we can apply it to real statistical data. Here is a good example:

```python
numbers = [12, 45, 67, 23, 89, 34, 56, 78, 90, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 150, 3, 9, 27, 81, 243, 12, 18, 24, 36, 48]

len_numbers = len(numbers) # Finding the number of items in the list

max_numbers = max(numbers) # Finding the maximum value

min_numbers = min(numbers) # Finding the minimum value

sum_numbers = sum(numbers) # Calculating the Sum of values

avg_numbers = sum_numbers / len_numbers # Calculating the average

print(f"Here is all the stats of the numbers: \n\tLength: {len_numbers}\n\tMax: {max_numbers}\n\tMin: {min_numbers}\n\tSum: {sum_numbers}\n\tMean: {avg_numbers}") # Displaying the values with f-string
```

The output:

```bash
$ python3 main.py
Here is all the stats of the numbers: 
        Length: 30
        Max: 243
        Min: 3
        Sum: 1741
        Mean: 58.03333333333333
```


