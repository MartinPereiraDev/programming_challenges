#method join

"""
To join a list into a string in Python, you can use the `join()` method, which
concatenates the elements of a list using a specified separator string. 
""" 

text = "Python is an interpreted language, which means that the code is executed line by line"
text_join_separator = '-'.join(text) # Use sepaparator - 
text_join = ' '.join(text)
print(text_join)
print(text_join_separator)