# Build 05 — Comments and putting it together

## Comments

A comment is a note in your code that Python ignores completely. It is there for humans.

Start a line with `#`:

```python
# This line does nothing at all
print("This line runs")
```

You can also put one at the end of a line:

```python
TAX_RATE = 0.20    # UK standard VAT rate
```

## Why bother

Two reasons, and the second is the real one.

When you work with other people, comments explain what a piece of code is for. When you work alone, comments explain it to **you in six months**, having forgotten everything.

That second case is the one that bites. Code you wrote yourself becomes unfamiliar faster than you expect.

## Comment the why, not the what

This is the mistake everyone makes at first:

```python
# Add 1 to the count
count = count + 1
```

The comment says exactly what the code already says. It adds nothing, and now there are two things to keep in sync.

Better:

```python
# Skip the header row, so start counting from 1
count = count + 1
```

That explains **why**, which the code cannot tell you on its own.

> [!TIP]
> If your code needs a comment to explain *what* it does, the better fix is usually a clearer variable name.
>
> ```python
> # Bad
> d = 86400   # seconds in a day
>
> # Good - no comment needed
> SECONDS_IN_A_DAY = 86_400
> ```

## Multiple lines

Python has no dedicated multi-line comment. Use `#` on each line:

```python
# This program works out the total cost
# of an order, including tax and delivery.
# Written for the week 1 lesson.
```

You will see triple-quoted strings used this way too:

```python
"""
This is technically a string, not a comment.
Python creates it and immediately throws it away.
"""
```

That works, but it is really meant for **docstrings** — descriptions at the top of a file or function. You will meet those properly later.

## Commenting out code

A common trick while testing. Put `#` in front of a line to stop it running, without deleting it:

```python
print("This runs")
# print("This does not")
print("This runs too")
```

In VS Code, select some lines and press `Ctrl + /` to toggle comments on all of them.

---

## Putting the week together

Everything from builds 01 to 05, in one small program:

```python
# A simple greeting program
# Week 1 - variables, strings, f-strings and maths

# Constants
GREETING = "Hello"
EXCLAMATION = "!"

# User details, with stray whitespace to clean up
first_name = "  john  "
last_name = "  DOE  "
birth_year = 2005
current_year = 2026

# Clean the input and build a full name
first_name = first_name.strip().title()
last_name = last_name.strip().title()
full_name = f"{first_name} {last_name}"

# Work out the age
age = current_year - birth_year

# Output
print(f"{GREETING}, {full_name}{EXCLAMATION}")
print(f"You are {age} years old.")
print(f"Your name is {len(full_name)} characters long.")
```

```
Hello, John Doe!
You are 21 years old.
Your name is 8 characters long.
```

Read through it and find each thing you learned this week: a constant in capitals, `.strip()` and `.title()` chained together, an f-string, subtraction, `len()`, and comments explaining the sections.

---

**Try it:** open `build-05.py`, then change the values and make it your own.
