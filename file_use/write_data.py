"""

To write data to a file in Python, you can use the ` write() ` method of the file object,
which writes a string to the file. Alternatively, you can use the ` writelines() ` method
to write a list of strings to the file. 
"""

# write a string to file
file = open(r"C:\Users\Administrador\workspace\Python\retosProgramacion\file_use\example.txt", "w")
file.write("Hello, world!\n")
file.close()


# write a list of strings to file
lines = ["This is the first line.\n", "This is the second line.\n", "This is the third line.\n"]
file = open(r"C:\Users\Administrador\workspace\Python\retosProgramacion\file_use\example.txt", "w")
file.writelines(lines)

file.close()