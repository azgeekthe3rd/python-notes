# Build 01 — Introduction to lists

## What is a list? 

A list **is a collection of ordered items, which can be of any data type (such as strings, numbers, or even other lists).** You can put anything you want inside a list: numbers, letters, names, usernames, grocery items—anything that comes to mind. Now you're probably asking yourself, **What is the point of a list?** You could write those things in your notepad, but you’d struggle to sort them if the list is large. This becomes even harder when you're working with huge databases that require sorting, compression, or mass adjustments. You’d also have a difficult time integrating that data with other Python libraries or software that tracks users, for example. So it’s vital to know how to use lists properly to become capable of building reliable applications.


## Building your first list

Your first list should look something similar to this:

```python

grocery_list = ['Milk', 'Butter', 'Ketchup', 'Eggs', 'Lettuce']
print(grocery_list)
```

As I've mentioned before, it's better to use descriptive names for the variables you're using. It helps keep things organized and avoids confusion.

This is what your output should look like:

```bash
$ python3 main.py
['Milk', 'Butter', 'Ketchup', 'Eggs', 'Lettuce']
```


## Returning specific elements from a list

Now, if you're interested in returning a single element from a list instead of printing the full list, you can simply tell Python to print the index if you know its position. Here's an example:


```python
grocery_list = ['Milk', 'Butter', 'Ketchup', 'Eggs', 'Lettuce']
print(grocery_list[0])
```

Output: 
```bash
$ python3 main.py
Milk
```

You can also apply string-type methods on top of it to make it look prettier. For example, we can use the string method _".upper()"_ to make the word we picked fully capitalized. Below is an example of that.


```python

grocery_list = ['Milk', 'Butter', 'Ketchup', 'Eggs', 'Lettuce']
print(f"Please don't forget the {grocery_list[0].upper()}!")
```

Output

```bash
$ python3 main.py
Please don't forget the MILK!
```

> [!NOTE]
> Index positions start at 0 not 1. So if you want to return the first value in a list you must set the index value to 0.


The following example returns specific elements from the list

```python
grocery_list = ['Milk', 'Butter', 'Ketchup', 'Eggs', 'Lettuce']
print(grocery_list[3])
print(grocery_list[4])
```

It should return the following output
```bash
$ python3 main.py
Eggs
Lettuce
```

> [!NOTE]
> If you wanted to print out the final item on a list you can simply put -1 instead of counting all the number of elements in the list.

## Printing the final item on a list

As I've mentioned in my previous note, if you want to return the final item of any list, you can always set the index value to `-1`. This works on any list as long as it's not empty. Read the warning below for more explanation.

```python
fruit_basket = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
print(fruit_basket[-1])
```
Output:

```bash
Elderberry
```
> [!WARNING]
> Mind you that if you were to leave the list empty or index a number that doesn't exist in the list, you get an error **stating that you are out of range**. You must always verify the number of elements using the len() function. Below is an example of what the error would look like when you try to run it.

```python
fruit_basket = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

print(fruit_basket[6]) # The index is clearly out of range.
```
Output: 
```console
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print(fruit_basket[6])
          ~~~~~~~~~~~~^^^
IndexError: list index out of range
```
**Try it:** open `build-01.py` and experiment with each method.