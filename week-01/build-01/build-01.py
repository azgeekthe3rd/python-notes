"""Build 01 - Variables and naming.

Run this file:  python build-01.py
"""

# --- Checking types ---------------------------------------------------------

print(type("Hello"))
print(type(42))
print(type(3.14))
print(type(True))

print()

# --- Your first variable ----------------------------------------------------

a = "Hello, world!"
print(a)

# --- More than one ----------------------------------------------------------

b = "This is my second variable"
print(b)

print()

# --- Reassigning ------------------------------------------------------------

message = "First value"
print(message)

message = "Second value"
print(message)

print()

# --- Good names vs bad names ------------------------------------------------

# Bad: tells you nothing
x = 24

# Good: tells you exactly what it holds
student_count = 24

print(student_count)
