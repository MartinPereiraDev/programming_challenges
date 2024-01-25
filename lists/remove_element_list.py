"""
In Python, there are multiple ways to remove an element from a list. Here are a few
common methods:

"""
"""
remove() method: The remove() method removes the first occurrence of a specified
element from the list. If the element is not found, it raises a ValueError.

"""
list = [1,2,3,4,5]
list.remove(2)
print(list)

"""
del statement: The del statement is used to remove an element from a list by its
index. It can also be used to remove a slice of elements from a list.

"""
list2 = [10,20,30,40,50]
del list2[2] # Del element list index 
print(list2)

"""
pop() method: The pop() method removes and returns an element from a list
based on its index. If no index is specified, it removes and returns the last element.
"""
list3 = [1,2,3,4,5]
list3.pop(4)
print(list3)