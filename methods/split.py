# method split()
"""
To split a string into a list in Python, you can use the ` split() ` method, which splits a
string into a list of substrings based on a specified delimiter. 

"""

text = "Python is dynamically typed, which means you don't need to declare variable types explicitly"
text_split = text.split()
text_split2 = text.split(',') # you can pass ',' as the delimiter to the split() method
print(text_split)
print(text_split2)
