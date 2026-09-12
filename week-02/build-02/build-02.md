# Build 02 — Modifying lists

## Overwriting elements in a list
Say you have a list full of elements and you want to replace a value within it. You can simply do the following:

```python
tech_accessories = ['USB Cable', 'Headphones', 'Mouse Pad', 'Power Bank']
print(tech_accessories) # Prints the original list before modifications.

tech_accessories[0] = 'TV' # Changing USB Cable -> TV 

print(tech_accessories) # Prints the new list
```

Output:
```bash 
$ python3 main.py
['USB Cable', 'Headphones', 'Mouse Pad', 'Power Bank']
['TV', 'Headphones', 'Mouse Pad', 'Power Bank']
```

## Modifying elements in a list

There are two ways you can add elements to a list. Each one behaves differently and has its own use. You can either `.append()` or `.insert()`. You will learn when to use each one as you go.

## Appending elements
When you append an element to a list, it gets added to the end of the list. You don't get to pick its position. However, people use it because it's the easiest way to add elements to a list stress-free. Here is an example:

```python
# Creating a list
tech_accessories = ['USB Cable', 'Headphones', 'Mouse Pad', 'Power Bank']

# Appending a new element to the list
tech_accessories.append("Wireless Charger")

print(tech_accessories) # Printing out the new list
```

Output

```bash
$ python3 main.py
['USB Cable', 'Headphones', 'Mouse Pad', 'Power Bank', 'Wireless Charger']
```

> [!NOTE]
> **.append()**, **.insert()**, **.sort()** and **.reverse()** all change the original list. They do not hand you a new one. sorted() is the exception, it leaves the original alone and gives you a new list back.

## Inserting elements to a list
As I've mentioned before, inserting lets you pick and choose where you want your new element added. **If you notice from the previous example, the new element we appended was added to the end of the list.**


```python
tech_accessories = ['USB Cable', 'Headphones', 'Mouse Pad', 'Power Bank']

tech_accessories.insert(2, "Telephone") # inserted at index 2, the third position

print(tech_accessories)
```

Output
```bash
$ python3 main.py
['USB Cable', 'Headphones', 'Telephone', 'Mouse Pad', 'Power Bank']
```

**Try it:** open `build-02.py` and experiment with each method.