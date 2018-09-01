#ASSIGNMENT- COMMON MODULES IN PYTHON

#Q.1- Print the current day using Datetime module.
import datetime
x=datetime.date.today()
print(x)
print('year is %d month is %s day is %d ' % (x.year,x.month,x.day))






#Q.2- Open your browser and play a video using webbrowser module in python.
import webbrowser
google = input('Enter video you want to see:')
webbrowser.open_new_tab('http://www.youtube.com/search?btnG=1&q=%s' % google)


#Q.3- Write a program to rename all the files in a directory and convert them into .jpg file format.
import os
os.rename('abc.txt','abc.jpg')
