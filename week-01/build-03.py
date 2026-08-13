"""Build 03 - F-strings and whitespace.

Run this file:  python build-03.py
"""

# --- Basic f-string ---------------------------------------------------------

name = "John"
print(f"Hello, {name}!")

print()

# --- Joining names ----------------------------------------------------------

first_name = "john"
last_name = "doe"

full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# --- Maths inside braces ----------------------------------------------------

price = 5
print(f"Two of those cost {price * 2}")

print()

# --- Escape characters ------------------------------------------------------

print("First line\nSecond line")
print("Name:\tJohn")
print("Languages:\n\tPython\n\tJava\n\tC")

print()

# --- Stripping whitespace ---------------------------------------------------

messy = "   hello   "

print(f"[{messy}]")
print(f"[{messy.lstrip()}]")
print(f"[{messy.rstrip()}]")
print(f"[{messy.strip()}]")

print()

# --- Removing prefixes and suffixes -----------------------------------------

url = "https://www.google.com"
print(url.removeprefix("https://"))

filename = "report.txt"
print(filename.removesuffix(".txt"))
