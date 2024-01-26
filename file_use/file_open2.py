"""
In this case open file and use to .read options file 
"""

# two cases open file use r when use "\" or use "\\" sin r 


# file_open = open(r"C:\Users\Administrador\workspace\Python\retosProgramacion\file_use\example.txt")

file_open = open("C:\\Users\\Administrador\\workspace\\Python\\retosProgramacion\\file_use\example.txt")
data = file_open.read()

print(data)


file_open.close()


