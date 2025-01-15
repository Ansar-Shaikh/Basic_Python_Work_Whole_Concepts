# A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusability.

def greet(name):
    """
    This function greets the person passed in as a parameter.
    """
    print(f"Hello, {name}!")

# Example usage
greet("Ansar")



#Parameters and Arguments : The terms parameter and argument can be used for the same thing: information that are passed into a function. But there is a difference:

#parameter is the variable listed inside the parentheses in the function definition.
#argument is the value that is sent to the function when it is called.

#arbitrary arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def arbitrary(*kids): 
    # *args is used to pass a variable number of arguments to a function. It allows you to take in more arguments than the number of formal arguments that you previously defined.
    print(f"The youngest child is {kids[2]}")

arbitrary("Sadhu", "Tohid", "Dolli")


#Keyword Arguments
#You can also send arguments with the key = value syntax.
def keyword(child3, child2, child1):
    print(f"The youngest child is {child3}")

keyword(child1 = "Sadhu", child2 = "Tohid", child3 = "Dolli")

#Recursion : Python also accepts function recursion, which means a defined function can call itself.
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#Factorial of a number using recursion
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
n=5
print("Factorial  of {n} ",factorial(5))