# Write a function that takes a dictionary and returns
# True if all values in the dictionary are unique, False otherwise.

dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated
dict3 = {} # Empty dictionary (all values are vacuously unique)

def unicf(di):

    stuni = set(di.values())
    if len(stuni) == len(di):
        print('True')
    else:
        print('False')

unicf(dict1)
unicf(dict2)
unicf(dict3)


