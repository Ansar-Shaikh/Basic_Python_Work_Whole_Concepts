#lambda fuctions are used to create small functions that are not needed to be defined by a standard function
#lambda arguments : expression
#The expression is executed and the result is returned:

#A lambda function in Python is an anonymous function defined with the lambda keyword. It can take any number of arguments but only contains a single expression. It is a small and restricted function having no more than one line.

#Example
#Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))    
#Output: 15

#Lambda functions can take any number of arguments:
#Example
x=lambda a,b,c:(a+b)*c
print(x(2,3,8))
#Output: 40

# it conatins only one expression but we can pass multiple arguments
#Example
x=lambda a,b:a+b
print(x(5,6))
#Output: 11
