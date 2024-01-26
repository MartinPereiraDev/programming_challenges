list_duplicate = [1,2,2,2,3,3,3,5,5,5,6,6,6,6]

# remove duplicate using set functions 

list_set = list(set(list_duplicate)) # set return a dictionary for defect

print ("Remove duplicate with set : ", list_set)

# remove duplicate using array

list_arr= []
for i in list_duplicate:
    if (i not in list_arr):
        list_arr.append(i)

print("Remove duplicate with arr : ", list_arr)

# remove duplicate with lambda

list_remove_lambda = lambda list_duplicate: list(set(list_duplicate))

print("Remove duplicate with lambda : ", list_remove_lambda(list_duplicate))


# remove duplicate form dictionary

dict_duplicate = {
    'car' : ['Ford', 'Toyota','Ford', 'Toyota'],
    'brand': ['Mustang', 'Ranz','Mustang', 'Ranz'],
}

dict_remove = {}

for key, value in dict_duplicate.items():
    dict_remove[key]= set(value)

print("Remove in dictionary duplicate : ", dict_remove)


# symmetric difference - Remove duplicate

set1 = {1,2,3,4,5,}
set2 = {3,5,2}

set_remove = set1.symmetric_difference(set2)

print("Remove symmetric difference : ", set_remove)