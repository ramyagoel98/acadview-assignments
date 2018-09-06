
# LIST COMPREHENSION & GENERATOR EXPRESSION

# Q.1- Write a python program to print the cube of each value of a list using list
# comprehension.
cube_list = []
l=[]
n=int(input('Enter number of elements'))
print('Enter the elements')
l=[int(input()) for i in range(0,n)]
cube_list=[i**3 for i in l]
print(l)
print(cube_list)

# Q.2- Write a python program to get all the prime numbers in a specific range using
# list comprehension.

prime_list=[x for x in range(1,10)  if all(x%i!=0 for i in range(2,x))]
print(prime_list)

# Q.3- Write the main differences between List Comprehension and Generator Expression.

'''
A list comprehension '[]' executes immediately and returns a list whereas a Generator
expression'()' return an object that can be iterated
Since a list is returned with list comprehension '[]' thus elements can be accessed
using indexes but an object is return in case of general expression '()' thus cannot
be accessed using indexes
'''

# LAMBDA & MAP

# Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using
# map and lambda expression.

cc= [39.2, 36.5, 37.3, 37.8]
f=[9/5*c+32 for c in cc]
print(f)

# Q.2- Apply an anonymous function to square all the elements of a list using map and
# lambda

n=int(input('Enter number of elements'))
sq_list = []
l=[]
print('Enter the elements')
l=[int(input()) for i in range(0,n)]
sq_list = list(map(lambda x : x*x , l))
print(sq_list)

# FILTER & REDUCE

# Q.1- Filter out all the primes from a list.

n=int(input('Enter number of elements'))
p_list = []
l=[]
print('Enter the elements')
l=[int(input()) for i in range(0,n)]
def prime(x):
    flag=0
    for i in range(2,x):
        if(x % i == 0):
            return False
    if (flag == 0):
        return True
p_list= list(filter(prime, l))
print(p_list)
               
# Q.2- Write a python program to multiply all the elements of a list using reduce.

from functools import *
n=int(input('Enter number of elements'))
mullist = []
l=[]
print('Enter the elements')
l=[int(input()) for i in range(0,n)]
mullist= reduce(lambda x,y : x*y, l)
print(mullist)
