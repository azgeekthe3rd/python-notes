# Week 1 — Getting set up

> Everything you need before writing a single line of code.

---

## Chapter 1

### What is Python?

Python is a high-level programming language created by **Guido van Rossum** in 1991. It is known for clear, English-like syntax and readability, which means you can usually write in a few lines what older languages need many more to express.

### What is the difference between Python versions?

Python versions come in two kinds:

| Type | What it does |
|------|--------------|
| **Major** | Introduces fundamental changes to how the language works |
| **Minor** | Adds new features and improves speed, without breaking what came before |

> [!IMPORTANT]
> You want **Python 3**. Python 2 reached end of life in 2020, and nothing new is written in it. If a tutorial uses `print "hello"` without brackets, it is Python 2 — close it.

### Why use Python?

Python is a common first language for people getting into programming, data science, web development, or task automation. It gets you to a working program quickly, without the overhead that languages like C or C# put in front of you before anything runs.

The syntax reads close to English, so your attention goes to the problem rather than to the rules of the language.

---

## Setting up

### 1. Install Python

<details>
<summary><b>Windows</b></summary>

```powershell
winget install Python.Python.3.13
```

</details>

<details>
<summary><b>macOS</b></summary>

```bash
brew install python
```

Requires [Homebrew](https://brew.sh) installed first.

</details>

<details>
<summary><b>Linux — Debian / Ubuntu</b></summary>

```bash
sudo apt update && sudo apt install python3 python3-pip
```

</details>

<details>
<summary><b>Linux — Fedora</b></summary>

```bash
sudo dnf install python3 python3-pip
```

</details>

### 2. Check it worked

```bash
python3 --version
```

On Windows, use `python --version` instead. You should see a version number printed back.

> [!WARNING]
> If you used the graphical installer on Windows, make sure you ticked **Add Python to PATH**. Missing it is the single most common reason the command is not recognised afterwards.

### 3. Install an editor

Python is on your machine now, but you still need somewhere to write code. That is what an **IDE** is for — an Integrated Development Environment, software for writing, editing and running code.

Install **[VS Code](https://code.visualstudio.com)**, then open the Extensions panel and install the **Python** extension by Microsoft.

> [!TIP]
> That is everything you need. Do not go hunting for more extensions yet — they will only get in your way.

---

## Your first program

Create a file called `hello.py` with one line in it:

```python
print("Hello, world!")
```

Run it from the terminal:

```bash
python hello.py
```

```
Hello, world!
```

If you see that, your setup works and you are ready to start.

---
---

<div align="center">

**Next:** [Week 1](../week-01/)

</div>