"""
Take a input from a user and print the table of 2
"""
table = input("Enter the number whose table to be printed \n")
table = int(table)
for i in range(1,11):
        print(table,'x',i,'=', i*table)


print("----------------------------------------")
#List the all the functions avaiable for the String Data Type.

help(str)