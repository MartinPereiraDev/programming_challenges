"""
In Python, the len() function is used to determine the length (number of elements) of various data structures,
such as strings, lists, tuples, dictionaries, and more

To find the length of a list in Python, you can use the `len()` function, which returns
the number of elements in the list.
"""

text = "Python emphasizes code readability and uses indentation (whitespace) to define code blocks"
text_len = len(text)
print("number of elements in text: ", text_len)

def pass_len(text):
    text_len = len(text)
    return text_len

text = "Python emphasizes code readability and uses indentation (whitespace) to define code blocks"
text_len = pass_len(text)
print("number of elements in text with pass_len function: ", text_len)
