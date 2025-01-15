# Identity Operators in Python
# 'is' operator
a = 10
b = 10
print(a is b) #True, because both a and b refer to the same object

# 'is not' operator
c = [1, 2, 3]
d = [1, 2, 3]
print(c is not d)  # True, because c and d refer to different objects

# Example with strings
e = "hello"
f = "hello"
print(e is f)  # True, because both e and f refer to the same string object

# Example with lists
g = [1, 2, 3]
h = g
print(g is h)  # True, because h is a reference to the same object as g