"""
To read data from a file in Python, you can use the ` read() ` method of the file object,
which reads the entire contents of the file as a string. Alternatively, you can use the
` readline() ` method to read one line of the file at a time. 

"""

file = open(r"C:\Users\Administrador\workspace\Python\retosProgramacion\file_use\example.txt", "r") # opens file for reading
data = file.read()
print(data)
file.close()


# read one line at a time
file = open(r"C:\Users\Administrador\workspace\Python\retosProgramacion\file_use\example.txt", "r")
line = file.readline()

while line:
    print(line)
    line = file.readline()

file.close()
