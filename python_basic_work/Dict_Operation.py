# Dictionary Operations in Python

# Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# Accessing values
print("Name:", my_dict['name'])  # Output: John
print("Age:", my_dict['age'])    # Output: 25

# Adding a new key-value pair
my_dict['email'] = 'ansarfshaikh2710@gmail.com'
print("Updated dictionary:", my_dict)

# Updating an existing key-value pair
my_dict['age'] = 26
print("Updated age:", my_dict['age'])  # Output: 26

# Removing a key-value pair
del my_dict['city']
print("Dictionary after deletion:", my_dict)

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists
if 'name' in my_dict:
    print("Name is present in the dictionary")

# Getting the length of the dictionary
print("Length of dictionary:", len(my_dict))

# Clearing all items in the dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)

#nested dictionary
my_dict = {
    'person1': {
        'name': 'John',
        'age': 25
    },
    'person2': {
        'name': 'Alice',
        'age': 30
    },
    'person3':[10,20,30,70]


}
print(my_dict['person1']['name'])  # Output: John
print(my_dict['person2']['age'])   # Output: 30
print(my_dict['person3'][2])   # Output: 30

#values() method
print("Values:", my_dict.values())

#keys() method
print(" keys:", my_dict.keys())
#iterating through dictionary
for i in my_dict:
    print(i,my_dict[i])