# Build 04 — Numbers and maths

## Integers and floats

Python has two number types you will use constantly.

| Type | What it is | Example |
|------|------------|---------|
| `int` | A whole number | `7`, `-3`, `1000` |
| `float` | A number with a decimal point | `3.14`, `-0.5`, `2.0` |

`2` and `2.0` are different types, even though they are the same value.

## The operators

| Operator | Does | Example | Result |
|----------|------|---------|--------|
| `+` | Add | `7 + 3` | `10` |
| `-` | Subtract | `7 - 3` | `4` |
| `*` | Multiply | `7 * 3` | `21` |
| `/` | Divide | `7 / 3` | `2.3333...` |
| `//` | Floor divide | `7 // 3` | `2` |
| `%` | Remainder | `7 % 3` | `1` |
| `**` | Power | `7 ** 3` | `343` |

```python
print(7 + 3)
print(7 - 3)
print(7 * 3)
print(7 / 3)
print(7 // 3)
print(7 % 3)
print(7 ** 3)
```

```
10
4
21
2.3333333333333335
2
1
343
```

## The three that catch people out

**`/` always gives a float.** Even when it divides evenly.

```python
print(10 / 2)
```

```
5.0
```

Note the `.0`. If you need a whole number, use `//`.

**`//` throws away the remainder.** It does not round — it always cuts downward.

```python
print(7 // 2)
```

```
3
```

**`%` gives you what is left over.** This is more useful than it looks. It is the standard way to check whether a number divides evenly:

```python
print(10 % 2)
print(11 % 2)
```

```
0
1
```

A result of `0` means it divided cleanly. That is how you test for even numbers.

## Floats are not exact

This surprises everyone the first time:

```python
print(0.1 + 0.2)
```

```
0.30000000000000004
```

That is not a bug in Python. Computers store decimals in binary, and some fractions cannot be represented exactly — the same way `1/3` cannot be written exactly in decimal.

It matters when comparing floats. `0.1 + 0.2 == 0.3` is `False`. For now, just know it happens.

## Large numbers

Long numbers are hard to read:

```python
population = 57128461853718
```

Underscores can be used as separators. Python ignores them entirely:

```python
population = 57_128_461_853_718
print(population)
```

```
57128461853718
```

The underscores are only there for your eyes. The stored value is identical.

## Assigning several variables at once

```python
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
```

```
1
2
3
```

The names on the left get matched up with the values on the right, in order. The counts must match.

## Constants

A constant is a value that should never change once set. Python has **no built-in way** to enforce this — there is no `const` keyword.

Instead there is a convention: **write the name in all capitals**. It has no effect on the code, but it signals to any reader that the value is not meant to be modified.

```python
FREEZING_POINT_C = 0
BOILING_POINT_C = 100
SECONDS_IN_A_DAY = 86_400

print(f"Water freezes at {FREEZING_POINT_C} degrees Celsius")
```

```
Water freezes at 0 degrees Celsius
```

Python will let you change it anyway. The capitals are a message to humans, not a rule.

---

**Try it:** open `build-04.py` and work through the operators.
