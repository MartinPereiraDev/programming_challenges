"""
In Python, the filter() function is a built-in function that allows you to filter elements
from an iterable (such as a list, tuple, or string) based on a specified condition. It
returns an iterator that yields the elements from the iterable for which the condition
evaluates to True. 
The filter() function applies the provided function to each element of the iterable
and returns an iterator that yields the elements for which the condition is True.

"""

def is_positive(n):
    return n > 0

numbers=[-10,52,-5,56,-85]

positive_numbers = filter(is_positive, numbers)

print(list(positive_numbers))
    