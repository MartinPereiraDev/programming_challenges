"""

file = open("fruits.txt")
# This will read the file in text mode by default
print(file.read())
# Close the file after reading
# It's a good practice to close the file after you're done with it
file.close()

"""


#Using 'with' statement to open a file
with open("files/fruits.txt") as file:
    # This will read the file in text mode by default
    content = file.read()
    print(content)
    # The file will be automatically closed after the with block

# Using 'a' mode to append to a file
with open("files/fruits.txt", "a") as file:
    # This will append to the file if it already exists or create a new one
    file.write("apple\nbanana\norange")
    
# Using 'w' mode to write to a file
with open("files/vegetables.txt", "w") as file:
    # This will overwrite the file if it already exists or create a new one
    file.write("tomato\nlettuce\npotato")    