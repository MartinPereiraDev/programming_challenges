"""
Dictionary comprehension is a similar concept to list comprehension, but instead
of creating lists, it allows you to create dictionaries in a concise way. You can
generate a new dictionary by specifying key-value pairs using an expression and
one or more for and if clauses. The basic syntax of dictionary comprehension is as
follows:
new_dict = {key_expression: value_expression for item in iterable if condition}
Let's break down the different parts:
1. key_expression: The expression to determine the keys of the new dictionary.
2. value_expression: The expression to determine the values of the new
dictionary.
3. item: A variable representing each item in the iterable.
4. iterable: A sequence that you want to iterate over, such as a list, tuple, or string.
5. condition (optional): A condition that filters the items based on a Boolean
expression. Only items for which the condition evaluates to True are included in
the new dictionary.
"""

squares = {x: x**2 for x in range(1,8)}
print(squares)