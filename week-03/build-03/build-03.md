# Build 03 — Slicing and copying lists

## Slicing a list

Say you wanted to print part of a list. Instead of all of it. Then you could use the slice method. Here is an example:

```python
ice_cream = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip", "Cookies and Cream", "Caramel Swirl", "Pistachio", "Mango", "Coffee"]

print(ice_cream[0:3])

```

Output:

```bash
$ python3 main.py
['Vanilla', 'Chocolate', 'Strawberry']
```

> [!NOTE]
> Python lists start at index 0, so when you slice a list, you don’t need to write the starting index if you want to begin from the first item. Writing [:5] means “start at index 0 and stop before index 5.”

Here are a couple more examples:

```python
mythical_creatures = ["Dragon", "Phoenix", "Unicorn", "Griffin", "Mermaid", "Hydra", "Centaur", "Minotaur", "Basilisk"]

print(f"Printing the first 4 items in the list: {mythical_creatures[:4]}")

print(f"Printing the last 4 items in the list: {mythical_creatures[-4:]}")


```

```bash
$ python3 main.py
Printing the first 4 items in the list: ['Dragon', 'Phoenix', 'Unicorn', 'Griffin']
Printing the last 4 items in the list: ['Hydra', 'Centaur', 'Minotaur', 'Basilisk']
```

## Copying a list
Sometimes you may want to back up a list or create two separate lists that behave independently. You can do so by applying the following method:
```python
ice_cream = ["Vanilla", "Chocolate", "Strawberry", "Mint"]

copy_ice_cream = ice_cream[:]   # this makes a real copy of the original list

print(copy_ice_cream)
```
Output:
```bash
$ python3 main.py
['Vanilla', 'Chocolate', 'Strawberry', 'Mint']
```

To prove that we actually created two separate lists, we can append different values to each one and then print both lists to show that they are no longer the same. Here is an example:
 
```python
ice_cream = ["Vanilla", "Chocolate", "Strawberry", "Mint"]

copy_ice_cream = ice_cream[:]

ice_cream.append("Oreo")

copy_ice_cream.append("Toffee")

print(ice_cream)
print(copy_ice_cream)
```

Output:
```bash
['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Oreo']
['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Toffee']
```