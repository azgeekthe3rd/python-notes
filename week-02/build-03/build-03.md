# Build 03 — Removing elements from a list

## Removing elements using the del statement

Say you are running a web service such as **Amazon** or **Netflix**. A user has been inactive for 8 years and you want to permanently delete the account. You can do so by using the `del` statement. Here is an example:

```python

study_essentials = ['Notebook', 'Pen', 'Sticky Notes', 'Calculator']

print(study_essentials) # Printing the original list

del study_essentials[0] # We delete the first element

print(study_essentials) # Printing out the modified list
```

Output
```bash
$ python3 main.py
['Notebook', 'Pen', 'Sticky Notes', 'Calculator']
['Pen', 'Sticky Notes', 'Calculator']
```

## Removing an item from a list using the pop() method

If you want to remove an item from a list *and also get its value*, you can use the `pop()` method. It removes the element from the list and returns it to you. 

A good way to imagine this is a stack of plates in your kitchen. When you pop a plate off the stack, you take the top plate (the last one added) and the stack becomes smaller.

```python
study_essentials = ['Notebook', 'Pen', 'Sticky Notes', 'Calculator']

last_item = study_essentials.pop()  # Removes the last item and returns it

print(last_item)        # Shows the item that was popped
print(study_essentials) # Shows the updated list
```
Output
```bash
$ python3 main.py
Calculator
['Notebook', 'Pen', 'Sticky Notes']
```
As you can see the output shows you that the final element was not included. You can also use this example in string methods. Here is an example:

```python
study_essentials = ['Notebook', 'Pen', 'Sticky Notes', 'Calculator']

last_item = study_essentials.pop() # Takes the final element out of the list

print(f"I forgot to bring my {last_item.lower()} for the exam.") # Formatting using string methods
```
Output
```bash
$ python3 main.py
I forgot to bring my calculator for the exam.
```

## Removing an item by name using .remove()
Now you're probably asking yourself why is this useful? We already have a couple of methods that do everything you probably need. However, if you're working with a large list where you'll probably make a mistake trying to count the position of a chosen element manually, you will need to use the `.remove()` method. This lets you specify the element you want removed just by name. Here is an example:


```python
study_essentials = ['Notebook', 'Pen', 'Sticky Notes', 'Calculator']

print(study_essentials) # Printing out the original list 

study_essentials.remove('Pen') # Naming the element we want removed 

print(study_essentials) # Printing the new list
```

Output:

```bash
$ python3 main.py
['Notebook', 'Pen', 'Sticky Notes', 'Calculator']
['Notebook', 'Sticky Notes', 'Calculator']
```

**Try it:** open `build-03.py` and experiment with each method.