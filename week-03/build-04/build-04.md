# Build 04 — Tuples

## What is a Tuple?
A tuple acts like a list. It looks like a list and can hold multiple items at once, but the key differences are that it uses parentheses instead of square brackets and you cannot change it or modify any of the items inside it. Here is a small example of how a tuple looks:

```python
my_tuple = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
print(my_tuple[0]) # Prints 2.
```
Output:

```bash
$ python3 main.py
2
```

I mentioned earlier that you cannot edit or replace values in a tuple the way you can in a list. The example below shows why this doesn’t work.

```python
my_tuple = (10, 100, 1000, 100000, 1000000) # Creating a tuple

my_tuple[2] = 30
```
Output
```bash
$ python3 main.py
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    my_tuple[2] = 30
    ~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

## Looping through values in a Tuple
If you want to loop through the values just like you do with lists, you can do the following:

```python
my_tuple = (1, 7, 2 ,5)

for number in my_tuple: # Looping through the tuple
    print(number)
```

The output:

```bash
$ python3 main.py
1
7
2
5
```
If we want to create a tuple with only one element, we must include a comma. Without the comma, Python will not treat it as a tuple. Here is how it should look:

```python
with_comma = (50,)
without_comma = (50)

print(with_comma)
print(without_comma)
```

Output:
```bash
$ python3 main.py
(50,)
50
```


## Writing over a Tuple
As we learned before, you cannot change or replace values inside a tuple. However, you can overwrite the entire tuple variable and assign new values to it.

```python
my_tuple = (15, 20)
print(my_tuple)

my_tuple = (50, 500)
print(my_tuple)
```


Output:
```bash
$ python3 main.py
(15, 20)
(50, 500)
```