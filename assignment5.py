#Q.1- Take an input year from user and decide whether it is a leap year or not.
y=int(input("enter year"))
if(y%4==0 and y%100!=0 or y%400==0):
    print("leap year")
else:
    print("not a leap year")


#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
l=int(input("enter l"))
b=int(input("enter b"))
if(l==b):
        print("dimension are of square")
else:
    print("dimension are of rectangle")
        
        
#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
a=int(input("enter age of 1 person "))
b=int(input("enter age of 2 person "))
c=int(input("enter age of 3 person "))
if(a>b and a>c):
    print("1 person is oldest")
elif (b>c and b>a):
    print("2 person is oldest")
else:
     print("3 person is oldest")
if(a<b and a<c):
    print("1 person is youngest")
elif (b<c and b<a):
    print("2 person is youngest")
else:
     print("3 person is youngest")   



#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 
#1. if employee is female, then she will work only in urban areas. 
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
#4. And any other input of age should print "ERROR". 
age=int(input(" enter age "))
sex=input(" enter M or F ")
ms=input(" enter Y or N ")
if(sex=='F'):
    print(" PLACE OF SERVICE IS:  urban area ")
elif(sex=='M' and (age>=20 and age<=40)):
    print(" PLACE OF SERVICE IS:  anywhere ")
elif(sex=='M' and (age>=40 and age<=60)):
    print(" PLACE OF SERVICE IS:  urban area ")
else:
    print("ERROR")
    

#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. 
qc=int(input("enter quantity"))
c=qc*100
if(c>1000):
    fc=c-(0.10*c)
else:
    fc=c
print("cost is",fc)




#qs6.............
l=[]
for i in range(0,10):
    x=int(input())#enter 10 numbers
    l.append(x)
print(l)

#qs 7........
#condition for infinite loop
#i=0
#while(i==0):
    #print("ramya")


#........qs8.................
l=[]
l2=[]
for i in range(0,10):
    x=int(input())#enter 10 numbers
    l.append(x)
    y=x*x
    l2.append(y)
print(l)
print(l2)



#qs9.......grup all datatypes
l=['ramya','rishabh','rajat',10,20,30,40,10.2,60.3]
f=[]
s=[]
intt=[]
for i in l:
    if(type(i)==str):
        s.append(i)
    elif(type(i)==int):
        intt.append(i)
    else:
        f.append(i)
print(l)
print(f)
print(intt)
print(s)





#qs10.............................
l=[]
for a in range(1,101):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        l.append(a)
print(l)






#qs 11......printing pattern
for i in range(0,4):
    for j in range(0,i+1):
        print('*',end="")
    print(' ')
        




#qs12.....
l=[]
for i in range(0,5):
    x=int(input("enter no"))
    l.append(x)
print(l)
s=int(input("enter value to be searched"))
for i in l:
    if(s==i):
        l.remove(i)

print(l)






    
