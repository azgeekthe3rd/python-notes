# Build 02 — Strings and string methods

## What is a string?

A string is a **sequence of characters** used to store and work with text. It can hold letters, numbers, symbols, punctuation and spaces.

You write one by wrapping it in quotes. Single or double both work, as long as you match them.

```python
a = "Hello, world!"
b = 'Single quotes work too'
```

Use double quotes if the text itself contains an apostrophe:

```python
sentence = "It's a nice day"
```

## String methods

A **method** is an action you can perform on a value. You call one by putting a dot after the variable, then the method name, then brackets.

```python
variable.method()
```

The brackets are required, even when empty.

| Method | What it does |
|--------|--------------|
| `.upper()` | Converts to UPPERCASE |
| `.lower()` | Converts to lowercase |
| `.title()` | Capitalises The First Letter Of Each Word |
| `.strip()` | Removes whitespace from both ends |
| `.lstrip()` | Removes whitespace from the left |
| `.rstrip()` | Removes whitespace from the right |
| `.replace(a, b)` | Swaps one piece of text for another |
| `.startswith(x)` | Returns True or False |
| `.endswith(x)` | Returns True or False |
| `len(x)` | Counts the characters (not a method — a function) |

## Using a method

Here is `.title()`:

```python
name = "john doe"
print(name.title())
```

```
John Doe
```

And `.lower()`:

```python
shout = "STOP SHOUTING"
print(shout.lower())
```

```
stop shouting
```

And `.upper()`:

```python
quiet = "hello"
print(quiet.upper())
```

```
HELLO
```

See the difference? The same piece of text, formatted three ways.

> [!IMPORTANT]
> Methods do not change the original variable. They return a **new** string.
>
> ```python
> name = "john"
> name.title()
> print(name)      # still "john"
> ```
>
> To keep the result, assign it back:
>
> ```python
> name = name.title()
> print(name)      # now "John"
> ```

## Counting characters

`len()` is a function, not a method, so the value goes inside the brackets:

```python
word = "Python"
print(len(word))
```

```
6
```

## Replacing text

```python
sentence = "I like cats"
print(sentence.replace("cats", "dogs"))
```

```
I like dogs
```

## Chaining methods

Methods can be strung together. Each one acts on the result of the last.

```python
messy = "   JOHN DOE   "
print(messy.strip().title())
```

```
John Doe
```

`.strip()` removes the spaces, then `.title()` fixes the capitalisation.

---

**Try it:** open `build-02.py` and experiment with each method.
