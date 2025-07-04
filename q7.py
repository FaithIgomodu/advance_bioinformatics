'''
Author: Faith Igomodu
Date: June 2, 2025
Instructions :

7) Write a program that takes user entered lines from the keyboard and stores them in an array. 
When the user enters "quit", the program prints out all the lines sorted (i.e. a line starting with 
an “Ab…” would print out before one starting with “Ac…”).
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
#7)
import numpy as np

user_lines = []
quit_word ='quit'
#prompt user to enter lines 
lines = int(input("How many lines will you enter?"))
#store lines in a list 
for letter in range(lines):
    text = input(f"Enter line {letter+1}:")
    user_lines.append(text)

#convert list to array
user_arr = np.array(user_lines)

arr_sort = sorted(user_arr)
#prompt user to enter quit
user_quit = input("Enter 'quit' to see the words sorted in alphabetical order:").strip().lower()
if user_quit == quit_word:
    print(f"The sorted lines are:{'\n'.join(arr_sort)}")

