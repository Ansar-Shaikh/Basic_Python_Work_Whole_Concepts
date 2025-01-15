# List Operations
"""

1. Creating a list:
    - A list named `my_list` is created with initial elements [1, 2, 3, 4, 5].
2. Adding an element to the end of the list:
    - The `append()` method is used to add the element 6 to the end of `my_list`.
3. Inserting an element at a specific position:
    - The `insert()` method is used to insert the element 10 at index 2 in `my_list`.
4. Removing an element from the list:
    - The `remove()` method is used to remove the first occurrence of the element 10 from `my_list`.
5. Popping an element from the list:
    - The `pop()` method is used to remove and return the last element of `my_list`.
6. Reversing the list:
    - The `reverse()` method is used to reverse the order of elements in `my_list`.
7. Sorting the list:
    - The `sort()` method is used to sort the elements of `my_list` in ascending order.
8. Getting the length of the list:
    - The `len()` function is used to get the number of elements in `my_list`.
Note: There is an error in the code where `my_list.length()` should be replaced with `len(my_list)`.
"""

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Adding an element to the end of the list
my_list.append(6)
print("After append:", my_list)

# Inserting an element at a specific position
my_list.insert(2, 10)
print("After insert:", my_list)

# Removing an element from the list
my_list.remove(10)
print("After remove:", my_list)

# Popping an element from the list
popped_element = my_list.pop()
print("After pop:", my_list)
print("Popped element:", popped_element)

# Reversing the list
my_list.reverse()
print("After reverse:", my_list)

# Sorting the list
my_list.sort()
print("After sort:", my_list)

# Getting the length of the list
length = my_list.length()
print("Length of the list:", length)