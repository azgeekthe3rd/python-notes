# Week 1 — Lab

> Everything here uses only what was covered in builds 01 to 05. No loops, no conditionals, no functions beyond what you have seen.

---

## How this works

1. Open `starter.py`. It has five tasks in it.
2. Fill in each one.
3. Run it and check your output against the expected output below.
4. Only look at `solution.py` once you have tried properly.

```bash
python starter.py
```

> [!TIP]
> Getting stuck is the part that teaches you. Reach for the lesson files before you reach for the solution.

---

## Task 1 — Clean the input

You are given a name with messy whitespace and inconsistent capitals:

```python
raw_name = "   aDA lOVELACE   "
```

Produce a clean version, capitalised properly, with no surrounding spaces.

**Expected output**

```
Ada Lovelace
```

---

## Task 2 — Build a greeting

Using the cleaned name from task 1, build a greeting with an f-string.

**Expected output**

```
Hello, Ada Lovelace! Welcome aboard.
```

---

## Task 3 — Work out a receipt

A customer buys **3** items at **£24.99** each. VAT is **20%**.

Work out the subtotal, the VAT amount, and the total. Store the VAT rate as a constant.

Print all three, each rounded to 2 decimal places.

> [!NOTE]
> To round to 2 decimal places inside an f-string, use `{value:.2f}`. This is the one thing in the lab that was not in the lessons.

**Expected output**

```
Subtotal: 74.97
VAT:      14.99
Total:    89.96
```

---

## Task 4 — Strip a URL

Take this URL and remove both the protocol at the front and the trailing slash at the end:

```python
url = "https://www.python.org/"
```

**Expected output**

```
www.python.org
```

---

## Task 5 — A formatted table

Given these three values:

```python
language = "python"
year = 1991
creator = "guido van rossum"
```

Produce the output below. Use `.title()` where it is needed, and `\t` for the spacing.

**Expected output**

```
Language:	Python
Year:	1991
Creator:	Guido Van Rossum
```

---

## Stretch task

Not required. Only if the five above felt easy.

Take a full name and produce initials with dots between them.

```python
name = "ada lovelace"
```

**Expected output**

```
A.L.
```

> [!TIP]
> Two new pieces here. `name.split()` breaks a string apart at the spaces, giving you the words separately. And `word[0]` gives you the first character of a string.

---

## Checking your work

Run your file and compare against the expected output above, line by line.

If you have pytest installed, you can check automatically:

```bash
pip install pytest
pytest test_lab.py
```

---

<div align="center">

**Back to:** [Week 1](../)

</div>
