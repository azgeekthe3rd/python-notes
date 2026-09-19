# Build 01 — Looping Through Lists


## Looping Through an Entire List
Say you want to print every element in a list separately, without showing the entire list like `ninja_moves = ['Punch', 'Kick', 'Flip', 'Block', 'Dash']`, or printing each item manually like `ninja_moves[0]`, `ninja_moves[1]`, `ninja_moves[2]`. This becomes repetitive, especially when working with a list that has many elements. This is where loops come in. You can print each element using a simple for‑loop. Here is an example:

```python
ninja_moves = ['Punch', 'Kick', 'Flip', 'Block', 'Dash']

for move in ninja_moves: # Iterate through each item in the list
    print(move) # This line creates a list of ninja moves and prints each one using a loop.
```

Output: 

```bash
$ python3 main.py
Punch
Kick
Flip
Block
Dash
```


> [!NOTE]
> You can name the loop variable anything you want, but it’s best to choose a name related to what each item represents to avoid confusion. In the previous example, ``move`` is just a variable name, I used it to make the code easier to read.

---

## Using f‑strings in loops
If you read last week’s lessons, you already know how to use f‑strings with individual list elements. In this section, we’re doing the same thing, but inside a loop. Here’s an example:

```python
names = ['Ali', 'Sara', 'Omar', 'Fatima', 'Hassan']

for name in names: # Iterate through each item in the inventory
    print(f"Hello, {name}, welcome to our society!") # Print each name in the list with our message
```

Output:

```bash
Hello, Ali, welcome to our society!
Hello, Sara, welcome to our society!
Hello, Omar, welcome to our society!
Hello, Fatima, welcome to our society!
Hello, Hassan, welcome to our society!
```

---
## Applying indentations properly

> [!NOTE]
> Avoiding indentation errors becomes easy once you get used to it. A standard indentation is about four spaces, but you don’t need to count them manually you can instead use the `tab` key on your keyboard. This is especially helpful when working with large loops that contain multiple nested blocks.
