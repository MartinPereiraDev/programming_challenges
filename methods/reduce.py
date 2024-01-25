"""
In Python, the reduce() function is a part of the functools module and is used for
performing a cumulative computation on a sequence of elements. It applies a
specified function to the elements of an iterable in a cumulative way, reducing the
sequence to a single value. To use the reduce() function, you need to import it from
the functools module:
from functools import reduce

"""

from functools import reduce

numbers = [12,2,5,8]

sum = reduce(lambda x, y: x * y, numbers)
print(sum)