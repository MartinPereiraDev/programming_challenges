"""
To check if an element is in a list in Python, you can use the in operator. The in
operator returns True if the element is found in the list and False otherwise.
Here's an example:

In this example, the element in my_list expression checks if element (which is set to
5) is present in my_list. Since 5 is in my_list, the condition is true, and the statement
"Element is in the list" is printed.

"""

list_find = [1,2,3,4,5,59,-12]
element = 5
if element in list_find:
    print("Element ", element, "  in the list ")
else:
    print("Element ", element, "not in the list ")