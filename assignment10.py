#Q.1- Write a Python program to read n lines of a file

f = open('test.txt','r')
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
#or simply we could use  f.read()
f.close()

#Q.2- Write a Python program to count the frequency of words in a file.
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))



#Q.3- Write a Python program to copy the contents of a file to another file
with open("test.txt",'r') as f:
    with open("ramya.txt", "w") as f1:
        for line in f:
            f1.write(line)
f=open("ramya.txt")
data=f.read()
print(data)

#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
f=open('file1.txt')
g=open('file2.txt')
j=open('newdoc.txt','w+')
h=f.readlines()
l=g.readlines()
for i,q in zip(h,l):
    j.write(str(i))
    j.write(str(q))
j.seek(0)
y=j.read()
print(y)

#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
f=open('test4.txt')
my_list=f.readline()
my_list=[int(i.strip()) for i in my_list]
my_list.sort()
my_list2=[]
for i in my_list:
    my_list2.append(str(i))
my_str='\n'.join((my_list2))
g=open('test5.txt','w')
g.write(my_str)
g.close()
f.close()



