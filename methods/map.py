
"""
The `map` function in Python applies a function to each element in a sequence and
returns a new sequence with the results. In Python, the map() function is a built-in
function that allows you to apply a given function to each element of an iterable
(such as a list , tuple , or string ) and returns an iterator that yields the results. It
100 Python Interview Questions & Answer For Data Science 5
provides a concise way to perform the same operation on every item in a collection
without writing explicit loops. 

"""
def multiply_by_two(n):
    return n * 2

numbers = [5,6,12,15,56]

result = map(multiply_by_two, numbers)

print(list(result))

