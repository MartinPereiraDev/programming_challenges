"""
A Python iterator is an object that can be used to iterate over a sequence of values.
It provides a __next__() method that returns the next value in the sequence, and
raises a StopIteration exception when there are no more values.

"""

class MyIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__ (self):
        return self

    def __next__ (self):
        if self.current < self.max_value:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

# Use the Iterator       
my_iter = MyIterator(1250)
for num in my_iter:
    print(num)

