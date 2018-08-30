#Regular Expressions:

    #Question 1: Valid Emaild Address:

import re as r

email = input("Enter the E-mail ID: ")
matcher = r.finditer('^[a-z][a-zA-Z0-9]*[@](gmail.com|yahoo.com)', email)
count = 0
for i in matcher:
    count += 1
if count == 1:
    print('Valid E-mail Address')
else:
    print('Invalid E-mail Address')



    #Question 2: Valid Phone Number:

import re as r

number = str(input('Enter the phone number: '))
matcher = r.finditer('^[+][9][1][-][6-9][\d]{9}', number)
count = 0
for i in matcher:
    count += 1
if count == 1:
    print('Valid Phone Number.')
else:
    print("Invalid Phone Number')
