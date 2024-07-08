"""
List comprehension is a concise way to create lists in Python. It allows you to
generate a new list by specifying an expression, followed by one or more for and if
clauses.
The basic syntax of list comprehension is as follows:
# syntax of list comprehension
new_list = [expression for item in iterable if condition]
Here's a breakdown of the different parts:
1. expression: The expression to be evaluated for each item in the iterable.
2. item: A variable that represents each item in the iterable.
3. iterable: A sequence, such as a list, tuple, or string, that you want to iterate
over.
4. condition (optional): A condition that filters the items based on a Boolean
expression. Only items for which the condition evaluates to True are included in
the new list.

"""

squares = [x**2 for x in range(1,20) if x > 5]
print(squares)

#  Selecting even numbers from 0 to 9 using list comprehension
even_numbers = [x for x in range(15) if x % 2 == 0]
print(even_numbers)

# Squaring numbers from 0 to 9 using list comprehension
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)


