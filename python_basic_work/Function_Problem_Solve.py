#write a function that takes three numbers and returns the maximum of the three numbers
def maximum(val1,val2,val3):
    if val1>val2 and val1> val3:
        return val1
    elif val2>val1 and val2>val3:
        return val2
    else:
        return val3
   
maximum(10,20,30)
# Output: 30    

#write a function that takes a list of numbers and returns the maximum of the list
def maximum_list(list):
    max = list[0]
    for i in list:
        if i>max:
            max = i
    return max

maximum_list([10,20,30,40,50])  
# Output: 50

#write a function that takes a list of numbers and returns the minimum of the list
def minimum_list(list):
    min = list[0]
    for i in list:
        if i<min:
            min = i
    return min

minimum_list([10,20,30,40,50])
# Output:10

def Create_Square_list(n):
    list=[]
    for i in range(1,n+1):
        list.append(i**2)
        return list
Create_Square_list(5)
# Output: [1,4,9,16,25]


#write a function it is prime or not
def prime(num):
    if num==1:
        print("It is not a prime number")
    if num==2:
        print("It is a prime number")
    if num>2:
        for i in range (2,num):
            if num % i==0:
                print("it is not prime number")
                break
        else:
            print("It is a prime number")   

prime(5)
prime(10)
# Output: It is a prime number    

