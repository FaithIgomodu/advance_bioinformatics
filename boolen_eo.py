'''
Author: Faith Igomodu
Date: 6/15/2025
Instructions:
Write a program that prompts the user for a number,
tests to see whether that number is even or odd
and prints out "Number is Even" if it is even,
or "Number is Odd" if it is odd. 
______________________________________________________________________________
Pseudocode 
Ask user for a number
use equality operator == to determine if even or odd
print results to std.output

'''


#Ask user for a number
user_num = int(input("Enter a number:"))

if user_num%2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    
