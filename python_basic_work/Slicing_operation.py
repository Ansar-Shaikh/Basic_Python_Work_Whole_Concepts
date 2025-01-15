# Slicing a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", my_list)
print("Sliced list (2:5):", my_list[2:5])
print("Sliced list (:-3):", my_list[:-3])
print("Sliced list (3:):", my_list[3:])
print("Sliced list with step (1:10:2):", my_list[1:10:2])

# Slicing a dictionary (Note: Dictionaries are unordered, so slicing is not directly applicable)
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print("Original dictionary:", my_dict)
keys = list(my_dict.keys())
sliced_keys = keys[1:4]
sliced_dict = {key: my_dict[key] for key in sliced_keys}
print("Sliced dictionary (1:4):", sliced_dict)

# Slicing a tuple
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Original tuple:", my_tuple)
print("Sliced tuple (2:5):", my_tuple[2:5])
print("Sliced tuple (:-3):", my_tuple[:-3])
print("Sliced tuple (3:):", my_tuple[3:])
print("Sliced tuple with step (1:10:2):", my_tuple[1:10:2])

# Output:
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Sliced list (2:5): [3, 4, 5]
# Sliced list (:-3): [1, 2, 3, 4, 5, 6, 7]
# Sliced list (3:): [4, 5, 6, 7, 8, 9, 10]
# Sliced list with step (1:10:2): [2, 4, 6, 8, 10]

# Original dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Sliced dictionary (1:4): {'b': 2, 'c': 3, 'd': 4}

# Original tuple: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Sliced tuple (2:5): (3, 4, 5)
# Sliced tuple (:-3): (1, 2, 3, 4, 5, 6, 7)
# Sliced tuple (3:): (4, 5, 6, 7, 8, 9, 10)
# Sliced tuple with step (1:10:2): (2, 4, 6, 8, 10)

#reverse slicing
reversed=my_list[::-1]
print("Reversed list:",reversed)
