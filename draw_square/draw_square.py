""" Function draw a square
"""
def square(num):
    init = ""
    write = "* "
    space= "  "
    middle = "* "
    calculation = num -2

    # This loop creates the top (and bottom) row of the square by repeating "* " num times.
    for n in range(num):
        init = init+write

    #This part prepares the middle rows.
    # It adds spaces to a to push the right side asterisk to the correct position.
    for s in range(calculation):
        write = space+write
    middle = middle + write       
    print(init)

    #This loop prints the middle rows of the square calculation times.
    for r in range (calculation):
        print(middle)
    print(init)    

# call with size of square
square(4)



