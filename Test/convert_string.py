"""
To convert a string to a number in Python, you can use the ` int() ` or ` float() `
function, depending on the type of number you want to convert to.
"""

my_string = "42"
my_int = int(my_string) # converts to integer
print(my_int) 

my_string = "3.14"
my_float = float(my_string) # converts to float
print(my_float) 
type = type(my_float)
print(type)


"""
To convert a number to a string in Python, you can use the ` str() ` function, which
returns a string representation of the number.

"""
my_int = 42
my_string = str(my_int) # converts to string
print(my_string) # outputs "42"

my_float = 3.14
my_string = str(my_float) # converts to string
print(my_string) # outputs "3.14"