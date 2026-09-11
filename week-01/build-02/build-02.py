"""Build 02 - Strings and string methods.

Run this file:  python build-02.py
"""

# --- Making strings ---------------------------------------------------------

a = "Hello, world!"
b = 'Single quotes work too'
sentence = "It's a nice day"

print(a)
print(b)
print(sentence)

print()

# --- Changing case ----------------------------------------------------------

name = "john doe"
print(name.title())

shout = "STOP SHOUTING"
print(shout.lower())

quiet = "hello"
print(quiet.upper())

print()

# --- Methods do not change the original -------------------------------------

original = "john"
original.title()
print(original)          # still lowercase

original = original.title()
print(original)          # now capitalised

print()

# --- Counting characters ----------------------------------------------------

word = "Python"
print(len(word))

# --- Replacing text ---------------------------------------------------------

line = "I like cats"
print(line.replace("cats", "dogs"))

# --- Chaining ---------------------------------------------------------------

messy = "   JOHN DOE   "
print(messy.strip().title())
