# tuples_operation.py

# Theory:
# A tuple is a collection which is ordered and unchangeable or immutable(that is it cant changeable through such operation ). 
# In Python, tuples are written with round brackets.
# Tuples are used to store multiple items in a single variable.

# Creating a tuple
my_tuple = ("apple", "banana", "cherry")
print("Original tuple:", my_tuple)

# Accessing elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Slicing a tuple
print("Sliced tuple (first two elements):", my_tuple[:2])

# Looping through a tuple
print("Looping through tuple:")
for item in my_tuple:
    print(item)

# Checking if an item exists
if "banana" in my_tuple:
    print("Yes, 'banana' is in the tuple")

# Tuple length
print("Length of tuple:", len(my_tuple))

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# Tuple with one item
single_item_tuple = ("apple",)
print("Single item tuple:", single_item_tuple)

# Unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print("Unpacked tuple:", green, yellow, red)

# Nested tuples
nested_tuple = (("a", "b", "c"), (1, 2, 3))
print("Nested tuple:", nested_tuple)

# Tuple methods
# count() - Returns the number of times a specified value occurs in a tuple
print("Count of 'apple' in my_tuple:", my_tuple.count("apple"))

# index() - Searches the tuple for a specified value and returns the position of where it was found
print("Index of 'banana' in my_tuple:", my_tuple.index("banana"))