"""Week 1 - Lab solutions.

Only read this after you have attempted the lab yourself.

There is more than one correct way to write most of these. If yours
produces the right output by a different route, yours is also correct.
"""

# =============================================================================
# Task 1 - Clean the input
# =============================================================================

raw_name = "   aDA lOVELACE   "

# .strip() removes the surrounding spaces, .title() fixes the capitals.
# Chaining them applies .title() to the result of .strip().
clean_name = raw_name.strip().title()

print(clean_name)


# =============================================================================
# Task 2 - Build a greeting
# =============================================================================

greeting = f"Hello, {clean_name}! Welcome aboard."

print(greeting)


# =============================================================================
# Task 3 - Work out a receipt
# =============================================================================

quantity = 3
price_each = 24.99

# All capitals marks this as a constant - a value not meant to change.
VAT_RATE = 0.20

subtotal = quantity * price_each
vat = subtotal * VAT_RATE
total = subtotal + vat

# {value:.2f} rounds to 2 decimal places for display.
print(f"Subtotal: {subtotal:.2f}")
print(f"VAT:      {vat:.2f}")
print(f"Total:    {total:.2f}")


# =============================================================================
# Task 4 - Strip a URL
# =============================================================================

url = "https://www.python.org/"

# Two separate jobs, so two methods chained together.
clean_url = url.removeprefix("https://").removesuffix("/")

print(clean_url)


# =============================================================================
# Task 5 - A formatted table
# =============================================================================

language = "python"
year = 1991
creator = "guido van rossum"

print(f"Language:\t{language.title()}")
print(f"Year:\t{year}")
print(f"Creator:\t{creator.title()}")


# =============================================================================
# Stretch task - Initials
# =============================================================================

name = "ada lovelace"

# .split() breaks a string apart wherever there is a space, giving you
# the pieces separately. first_part is "ada", second_part is "lovelace".
first_part, second_part = name.split()

# [0] takes the first character of each piece.
initials = f"{first_part[0].upper()}.{second_part[0].upper()}."

print(initials)
