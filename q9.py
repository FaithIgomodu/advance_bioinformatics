'''
Author: Faith Igomodu
Date: June 2, 2025
Instructions:


9) Ask the user for a list of sequence lengths, separated by whitespace (Example: 100  123  45 
…etc.). Store the sequence lengths as one string in a variable, then: 
a) Split that string and create an array from it (each number being an element of the array) 
b) Use a for loop to get the sum of all sequence lengths. 
c) Print the average.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
#9)
import numpy as np 

#prompt user for input
user_input = input("\nEnter a list of sequence length separated by white space").split()

#a)
user_arr = np.array(user_input, dtype= int)
user_len = user_arr.size

#b)
total = 0
for val in user_arr:
    total += val
#c)
print("\nThe mean length  of the list of sequences is:", total/user_len)
    
