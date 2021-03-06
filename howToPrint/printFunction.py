#created file on windows OS

#including header file
import sys
import os
import datetime
import time

from datetime import datetime

osName = os.name 
#print without using quotes
print(os.name)      
print(40)     

#print with double quotes 
print("Hello World")     

#print with single quotes
print('Hello World 2')   

#print single quote with string as well 
print("Hello World 3, it's python") 

#print double quotes with string as well
print('"Quality means doing it right when no one is looking." – Henry Ford') 

#print a quote along with double quotes in a string
print('''"When Henry Ford made cheap, reliable cars, people said, 'Nah, what's wrong with a horse?' That was a huge bet he made, and it worked." - Elon Musk ''')


#print without new line character , end ='' (end ='' will add last character as '', end='\n' will add the new line character at the end of the string
print('Stay Productive, ' , end='') 
print('Do Workout daily ' , end='\n')

#print with seperator | between multiple strings  
print('Eat ','Fruits ', 'and ' ,'keep ', 'Smiling ', 7,  sep='|') 

#print with formatting
print(f'Operating system name is : {osName}') 

#printing today's datetime 
print(datetime.today()) 

#open file in write mode with UTF-8 encoding 
sample= open(r'.\a.txt','w',encoding='utf-8')
print(sample)

#print the output to the file instantly with flush = True 
for i in range(10):
    print("Drink water", file= sample , flush =True) 
    time.sleep(5)

# #print the output to the file with buffering when flush = False 
# #by default flush parameter is set to False
for i in range(10):
    print("Eat fruits", file= sample) 
    time.sleep(5)