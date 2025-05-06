"""

file = open("fruits.txt")
# This will read the file in text mode by default
print(file.read())
# Close the file after reading
# It's a good practice to close the file after you're done with it
file.close()

"""


#Using 'with' statement to open a file
with open("fruits.txt") as file:
    # This will read the file in text mode by default
    content = file.read()
    print(content)
    # The file will be automatically closed after the with block