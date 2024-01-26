"""
To randomize the items of a list in place (modifying the original list), you can
make use of the random.shuffle() function from the random module in Python. The
100 Python Interview Questions & Answer For Data Science 11
shuffle() function shuffles the elements of a list randomly. 

"""
import random as rdm


my_list = [1,10,20,30]

rdm.shuffle(my_list)

print(my_list)