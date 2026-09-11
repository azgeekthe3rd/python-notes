# Build 01 — Variables and naming

## What is a variable?

A variable is a **name that points to a value stored in memory**. You give the value a label, and from then on you can use the label instead of repeating the value.

If that sounds abstract, it will make sense the moment you use one. Keep reading.

## Simple data types

A data type describes what kind of value you are storing. Python works out the type for you — you never declare it.

| Type | Name | Example | What it holds |
|------|------|---------|---------------|
| `str` | String | `"Hello"` | Text |
| `int` | Integer | `42` | Whole numbers |
| `float` | Float | `3.14` | Decimal numbers |
| `bool` | Boolean | `True` | True or False |
| `list` | List | `[1, 2, 3]` | An ordered collection |
| `dict` | Dictionary | `{"a": 1}` | Key and value pairs |
| `NoneType` | None | `None` | Nothing |

The first four are covered this week. Lists and dictionaries come later.

You can check the type of anything with `type()`:

```python
print(type("Hello"))
print(type(42))
print(type(3.14))
```

```
<class 'str'>
<class 'int'>
<class 'float'>
```

## Naming rules

Python will refuse to run if you break these.

| Rule | Why |
|------|-----|
| Letters, numbers and underscores only | No spaces, dashes or symbols |
| Cannot start with a number | `2fast` is invalid, `fast2` is fine |
| No spaces | Use an underscore instead |
| Cannot be a reserved keyword | `class`, `if`, `for` and so on are taken |
| Case sensitive | `name` and `Name` are two different variables |

## Valid and invalid names

| Valid | Invalid | Why it fails |
|-------|---------|--------------|
| `name` | `2name` | Starts with a number |
| `first_name` | `first name` | Contains a space |
| `user2` | `user-2` | Contains a dash |
| `_private` | `class` | Reserved keyword |
| `total_price` | `total price!` | Space and symbol |

> [!TIP]
> Names should describe what they hold. `student_count` tells you something. `x` does not. You will thank yourself in six months.

## Your first variable

In the last lesson you ran this:

```python
print("Hello, world!")
```

That printed the text directly. Now store it in a variable first:

```python
a = "Hello, world!"
print(a)
```

```
Hello, world!
```

That is your first variable.

Breaking it down: `a` is the variable name. The `=` assigns. `"Hello, world!"` is the value being stored.

> [!WARNING]
> Python is case sensitive. `print()` works, `Print()` does not. The same goes for your own variable names.

## More than one

You can create as many as you need:

```python
a = "Hello, world!"
print(a)

b = "This is my second variable"
print(b)
```

```
Hello, world!
This is my second variable
```

Each `print()` puts its output on a new line.

## Changing a value

A variable can be reassigned at any time. The old value is discarded.

```python
message = "First value"
print(message)

message = "Second value"
print(message)
```

```
First value
Second value
```

---

**Try it:** open `build-01.py`, run it, then change the values and run it again.
