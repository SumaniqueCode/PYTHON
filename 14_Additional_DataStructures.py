# Created on 2024/01/31
# By Suman Regmi

# Tuples are just like lists, but the difference is tuples are immutable.
# It means you cannot change or add any items to the tuple.
# Tuples are generally written inside () and are seperated by comma.
# The way of indexing or accessing the items in tuple is also as same as list

tuple = ("Tuple Example", 5.254, 1)
print(tuple)
print(tuple[0:])

# Sets can be used instead of list if we know the elements.
# They are also immutable.
# They are unordered collection of items with no duplicates.
# Sets are generally written inside {} and are seperated by comma.
# The way of indexing or accessing the items in set is also as same as list

set = {9 ,  "Python", True}
print(set)
print("Length of set: ", len(set))


# Dictionary is a collection of key value pairs.
# Dictionaries are generally written inside {} and are separated by colon(:).
# Key must be unique while values can have duplicate entries.

dictionary = {"Name": "Suman", "Age" : 26, "Country":"Nepal"}
print(dictionary["Name"])
print(dictionary.get("City"))   # Returns None if there is no such key present in dictionary
print(dictionary.keys())        # Gives all keys present in the dictionary
print(dictionary.values())      # Gives all values present in the dictionary
print(dictionary.items())       # Gives both keys and values present in the dictionary