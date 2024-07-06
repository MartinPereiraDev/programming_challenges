""" Function draw a square
"""
def square(num):
    z = ""
    a = "* "
    space= "  "
    l = "* "
    calculation = num -2
    for n in range(num):
        z = z+a
    for s in range(calculation):
        a = space+a 
    l = l + a       
    print(z)
    for r in range (calculation):
        print(l)
    print(z)    
    

square(35)


