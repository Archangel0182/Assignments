#split(): This method splits a string into a list of substrings based on a specified delimiter. By default, it splits the string on whitespace.
text = "Hello, World!"
words = text.split()
print(words)  # Output: ['Hello,', 'World!']

#strip(): This method removes leading and trailing whitespace from a string.
text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"

#replace(): This method replaces occurrences of a substring within a string with another substring.
text = "Hello, World!"
new_text = text.replace("Hello", "Hi")
print(new_text)  # Output: "Hi, World!"

#center(): This method centers a string within a specified width by padding it with a specified character. It returns a new string.
text = "Hello"
centered_text = text.center(10, "*")
print(centered_text)  # Output: "**Hello***"

#title(): This method capitalizes the first character of each word in a string.
text = "hello, world!"
title_text = text.title()
print(title_text)  # Output: "Hello, World!"
