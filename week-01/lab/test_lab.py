"""Automatic checks for the week 1 lab.

Run with:  pytest test_lab.py

These test the same things the expected output in lab.md shows, so if
your answers match the output, these will pass.
"""

from __future__ import annotations


class TestTask1:
    def test_strips_and_capitalises(self) -> None:
        raw_name = "   aDA lOVELACE   "
        assert raw_name.strip().title() == "Ada Lovelace"


class TestTask2:
    def test_greeting_format(self) -> None:
        clean_name = "Ada Lovelace"
        greeting = f"Hello, {clean_name}! Welcome aboard."
        assert greeting == "Hello, Ada Lovelace! Welcome aboard."


class TestTask3:
    def test_receipt_maths(self) -> None:
        quantity = 3
        price_each = 24.99
        VAT_RATE = 0.20

        subtotal = quantity * price_each
        vat = subtotal * VAT_RATE
        total = subtotal + vat

        assert f"{subtotal:.2f}" == "74.97"
        assert f"{vat:.2f}" == "14.99"
        assert f"{total:.2f}" == "89.96"


class TestTask4:
    def test_url_stripped_both_ends(self) -> None:
        url = "https://www.python.org/"
        assert url.removeprefix("https://").removesuffix("/") == "www.python.org"


class TestTask5:
    def test_table_rows(self) -> None:
        language = "python"
        year = 1991
        creator = "guido van rossum"

        assert f"Language:\t{language.title()}" == "Language:\tPython"
        assert f"Year:\t{year}" == "Year:\t1991"
        assert f"Creator:\t{creator.title()}" == "Creator:\tGuido Van Rossum"


class TestStretch:
    def test_initials(self) -> None:
        name = "ada lovelace"
        first_part, second_part = name.split()
        initials = f"{first_part[0].upper()}.{second_part[0].upper()}."
        assert initials == "A.L."
