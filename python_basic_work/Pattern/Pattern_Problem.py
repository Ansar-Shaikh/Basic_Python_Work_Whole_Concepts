# Pattern 1: Right-angled triangle
def pattern1(n):
    for i in range(1, n+1):
        print('*' * i)

# Pattern 2: Inverted right-angled triangle
def pattern2(n):
    for i in range(n, 0, -1):
        print('*' * i)

# Pattern 3: Pyramid
def pattern3(n):
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' * (2*i-1))

# Pattern 4: Diamond
def pattern4(n):
    for i in range(1, n+1):
        print(' ' * (n-i) + '*' * (2*i-1))
    for i in range(n-1, 0, -1):
        print(' ' * (n-i) + '*' * (2*i-1))

# Pattern 5: Square
def pattern5(n):
    for i in range(n):
        print('*' * n)

# Example usage
n = 5
pattern1(n)
print()
pattern2(n)
print()
pattern3(n)
print()
pattern4(n)
print()
pattern5(n)