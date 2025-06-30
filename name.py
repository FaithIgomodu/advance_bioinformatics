'''

Author: Faith Igomodu
Date: June 27, 2025
Description:
Write a function that takes user name as input and returns it 

'''


def print_name():
    '''
    Function accepts a string and return it 
    
    
    arg:
    ----
    none, user input is obtained. 


    return:
    ------
    name 

    '''
    
    #obtain user name 
    name = input("What is your name?: ")
    #return name
    return name

#use case
user_name = print_name()
print("Hi", user_name)
