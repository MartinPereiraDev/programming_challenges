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

"""
Read and split data with os.open

"""
file_split = open("C:\\Users\\Administrador\\workspace\\Python\\retosProgramacion\\file_use\example.txt")

data = file_split.read()
print("Data read : \n",data)

data_split = data.split('\n')
print("Data Split : ",data_split)

file_split.close()
