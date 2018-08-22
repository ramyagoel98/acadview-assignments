#Q.1- Create a function to calculate the area of a sphere by taking radius from user.
def aos(r):
    a=4*3.14*r*r
    return a

radius=int(input("enter radius of sphere"))
area=aos(radius)
print("area of sphere " ,area)




#Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].
def perfect():
    for x in range(1,1001):
        a=1
        sum=0
        while(a<=int(x/2)):
              if(x%a==0):
                  sum+=a
              a+=1
        if(sum==x):
              print(x)
perfect()



#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user. Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
t=int(input("enter no whose table u want to find"))
for i in range(1,11):
    p=t*i
    print(t,"*",i,"=",p)


     



#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def pon(a,b):
    if(b!=0):
        b=b-1;
    elif(b==0):
        return 1
    return a*pon(a,b)
a=int(input("enter base no"))
b=int(input("enter power no to be raised"))
print(pon(a,b))

