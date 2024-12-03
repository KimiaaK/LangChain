"""Given the string text, return True if it is a palindrome, else False.
After lowering all letters and removing all non-alphanumeric characters,
the word should read the same forward and backward."""

import re


def is_Palindrome(text):
    text = text.lower()  # make them all lowercased
    cleaned = re.compile("\W+")
    text = cleaned.sub("", text).strip()  # removes non-alphanumerics
    return text == text[::-1]


# Test cases
List = ["Anna", "**Radar****", "Abid", "(Level)", "Data"]

for text in List:
    print(f"Is {text} a palindrome?\n {is_Palindrome(text)}")
