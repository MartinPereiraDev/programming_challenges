"""
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
 usually starting with 0 and 1. 
 The sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so forth.
"""

def fib_gen():
    a = 0 
    b = 1 
    while True:
        c = a 
        a = b 
        b = c+a
        yield c 

f = fib_gen()
print(next(f))
for i in range(20):
    print(next(f), end=' ')
