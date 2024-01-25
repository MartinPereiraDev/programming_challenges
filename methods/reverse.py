"""
To reverse a list in Python, you can use either the reverse() method or slicing .
Here's how you can use each method:
100 Python Interview Questions & Answer For Data Science 18
reverse() method: The reverse() method is a list method that reverses the order of
the elements in the list in place, meaning it modifies the original list.

"""

my_list = [2,5,12,65,98,3]

my_list.reverse() # reverse list in the place 
print(my_list) 

"""
Slicing: You can reverse a list using slicing by specifying the step value as -1, which
traverses the list in reverse order. This method returns a new reversed list without
modifying the original list
"""
my_list2 = [1,10,20,30,50,70]
reversed_list = my_list2[::-1] # Returns a new reverser list 
print(reversed_list)
print(my_list2) # Origianl list is unchanged