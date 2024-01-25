"""
To sort a list in Python, you can use the ` sorted() ` function, which returns a new
sorted list, or the ` sort() ` method, which sorts the list in-place. Both functions take
an optional ` key ` parameter, which is used to specify a function that returns a value
to use for sorting.

"""

my_list= [1,5,6,8,12,4]
my_list.sort() # Sorts the list ins ascending order
print(my_list)

# Sort the lis in descending order, pass the parameter as True
my_list.sort(reverse=True)
print(my_list)

my_list2= [85,11,6,83,12,4]
sorted_list = sorted(my_list2) # return a new sorted List
print(sorted_list)
print("original list: ", my_list2)

# TO sort list in descending order, use the reverse parameter
sorted_list_desc = sorted(my_list2, reverse=True)
print("Lsit ordering descending : ", sorted_list_desc)

