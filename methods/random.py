"""
To randomize the items of a list in place (i.e., modifying the original list), you can
make use of the random.shuffle() function from the random module in Python. The
100 Python Interview Questions & Answer For Data Science 11
shuffle() function shuffles the elements of a list randomly. 

"""
import random


my_list = [1,10,20,30]

random.shuffle(my_list)

print(my_list)