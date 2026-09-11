# Build 03 — F-strings and whitespace

## What is an f-string?

An f-string is a quick way to drop variables straight into a sentence, without messing about with commas or plus signs.

You make one by putting `f` in front of the opening quote, then wrapping any variable in curly braces.

```python
name = "John"
print(f"Hello, {name}!")
```

```
Hello, John!
```

## Why they exist

Before f-strings, joining text and variables was clumsy:

```python
# Old way - concatenation
full_name = first_name + " " + last_name

# Old way - .format()
full_name = "{} {}".format(first_name, last_name)

# Modern way - f-string
full_name = f"{first_name} {last_name}"
```

The f-string version is shorter and you can read it straight through.

> [!NOTE]
> F-strings arrived in Python 3.6. Any version you install today has them.

## A worked example

```python
first_name = "john"
last_name = "doe"

full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
```

```
Hello, John Doe!
```

Two things happening there. The first f-string joins the names together. The second calls `.title()` **inside** the braces, so the capitalisation is fixed on the way out.

You can run any method or calculation inside the braces:

```python
price = 5
print(f"Two of those cost {price * 2}")
```

```
Two of those cost 10
```

## Whitespace

Whitespace means any character you cannot see — spaces, tabs and newlines. Python has escape characters for the invisible ones.

| Escape | What it does |
|--------|--------------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | A literal backslash |
| `\"` | A literal double quote |

```python
print("First line\nSecond line")
```

```
First line
Second line
```

```python
print("Name:\tJohn")
```

```
Name:	John
```

```python
print("Languages:\n\tPython\n\tJava\n\tC")
```

```
Languages:
	Python
	Java
	C
```

## Stripping whitespace

Text from a user or a file often arrives with unwanted spaces on the ends. Three methods deal with it.

| Method | Removes from |
|--------|--------------|
| `.lstrip()` | The left |
| `.rstrip()` | The right |
| `.strip()` | Both ends |

```python
messy = "   hello   "

print(f"[{messy}]")
print(f"[{messy.lstrip()}]")
print(f"[{messy.rstrip()}]")
print(f"[{messy.strip()}]")
```

```
[   hello   ]
[hello   ]
[   hello]
[hello]
```

The square brackets are there so you can see where the text actually starts and ends.

> [!TIP]
> `.strip()` on user input is a habit worth forming early. People type stray spaces constantly, and `"john "` and `"john"` are two different strings as far as Python is concerned.

## Removing a prefix

Say you have a URL and want the `https://` gone:

```python
url = "https://www.google.com"
print(url.removeprefix("https://"))
```

```
www.google.com
```

There is a matching `.removesuffix()`:

```python
filename = "report.txt"
print(filename.removesuffix(".txt"))
```

```
report
```

> [!WARNING]
> `.removeprefix()` and `.removesuffix()` need Python 3.9 or newer. If you installed recently you are fine.

---

**Try it:** open `build-03.py` and change the strings to see what happens.
