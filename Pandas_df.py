import pandas as pd 
import os

classrom = input('Enter student classrom\n')
gender = input('Enter student gender\n')
name = input('Enter student name\n')
age = input('Enter student age\n')

#Creating dataFrame from inputed variables
df = pd.DataFrame({'Classrom':[classrom], 'Gender':[gender], 'Name':[name], 'Age':[age]}, columns=['Classrom', 'Gender', 'Name', 'Age'])

if os.path.isfile('./students.csv'): #Checkin is file already in folders
    df.to_csv('students.csv', mode='a', header=False)#if yes then apend student without headers
else: #if not then make file and apend headers + student credentials
    df.to_csv('students.csv', mode='a')#Writing to a file