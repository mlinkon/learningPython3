#created file on windows OS

#including header file

import os
import datetime

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
print('"Hello World 4"') 

#print without new line character , end ='' (end ='' will add last character as '', end='\n' will add the new line character at the end of the string
print('Hello World 5 ' , end='') 
print('Hello World 6 ' , end='\n')

#print with seperator | between multiple strings  
print('Hello ','World ', 7,  sep='|') 

#print with formatting
print(f'Operating system name is : {osName}') 

#printing today's datetime 
print(datetime.today()) 
