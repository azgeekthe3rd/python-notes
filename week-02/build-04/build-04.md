# Build 04 — Organizing lists

Keeping your lists organized is important for many reasons. You don’t want your code breaking later. Messy lists can lead to wrong indexes, unexpected values, and bugs that are hard to track. Keeping your list organized also helps you find things more easily. If you want to sort a list permanently you can use the `.sort()` method. It sorts your list in an alphabetical order.


```python
travel_essentials = ['Passport', 'Boarding Pass', 'Travel Pillow', 'Water Bottle', 'Phone Charger']

travel_essentials.sort() # Sorting the list into an alphabetical order

print(travel_essentials) # Printing the list
```

Output:
```bash
$ python3 main.py
['Boarding Pass', 'Passport', 'Phone Charger', 'Travel Pillow', 'Water Bottle']
```

> [!NOTE]
> Sorting isn't purely alphabetical. Capitals sort before lowercase letters, because Python compares character codes.

Now, if you want the list to be sorted in reverse alphabetical order, you can set the `reverse` argument to `True`. Here is a clear example:

```python
travel_essentials = ['Passport', 'Boarding Pass', 'Travel Pillow', 'Water Bottle', 'Phone Charger']

travel_essentials.sort(reverse=True) # Sorting the list into a reverse-alphabetical order

print(travel_essentials) # Printing the new list
```
Output:
```bash
['Water Bottle', 'Travel Pillow', 'Phone Charger', 'Passport', 'Boarding Pass']
```

## Sorting out lists temporarily with the `sorted()` function

If you wanted to sort out a list temporarily instead of permanently then you can use the `sorted()` function. It lets you display a list in whatever order you want without affecting the actual order of the list. Below I included an example

```python
travel_essentials = ['Water Bottle', 'Travel Pillow', 'Phone Charger', 'Passport', 'Boarding Pass']

print("Here is the original list: ")
print(travel_essentials)

print("Here is the sorted list: ")
print(sorted(travel_essentials))

print("Here is the original list again: ")
print(travel_essentials)
```

Here is what the output is going to look like. As you can see the list isn't sorted permanently:
```bash
$ python3 main.py
Here is the original list: 
['Water Bottle', 'Travel Pillow', 'Phone Charger', 'Passport', 'Boarding Pass']
Here is the sorted list: 
['Boarding Pass', 'Passport', 'Phone Charger', 'Travel Pillow', 'Water Bottle']
Here is the original list again: 
['Water Bottle', 'Travel Pillow', 'Phone Charger', 'Passport', 'Boarding Pass']
```

> [!NOTE]
> A couple steps back I've shown you how you can reverse the order of a list. However, if you simply want to flip the list backwards without sorting it, you can use the `.reverse()` method. It's explained below, but you must understand the difference between the two to use them effectively.

## Printing a list in reverse order
Now as I've mentioned in the previous note, if you want to essentially reverse the order of the current list you must apply the `.reverse()` method. Here is a good example showing you how it works:


```python
travel_essentials = ['Water Bottle', 'Travel Pillow', 'Phone Charger', 'Passport', 'Boarding Pass']

travel_essentials.reverse()   # This reverses the list

print(travel_essentials)      # This shows the reversed list

```
Output:
```bash
$ python3 main.py
['Boarding Pass', 'Passport', 'Phone Charger', 'Travel Pillow', 'Water Bottle']
```


## Finding the Length of a List

If you're interested in finding the length of a list without manually counting each item, you can simply use the `len()` function. It helps speed up the process rather than spending time doing it. Here is an example:

```python
travel_essentials = ['Water Bottle', 'Travel Pillow', 'Phone Charger', 'Passport', 'Boarding Pass']

print(len(travel_essentials))
```

Output:

```bash
$ python3 main.py
5
```


**Try it:** open `build-04.py` and experiment with each method.