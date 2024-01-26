
def bs(a):
# a = name of list
    b=len(a)
# minus 1 because we always compare 2 adjacent values
    for x in range(b):
        for y in range(b-x):
            a[y]=a[y+1]
 
a=[32,5,3,6,7,54,87]
bs(a)