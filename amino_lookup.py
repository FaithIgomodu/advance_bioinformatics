'''
Author: Faith Igomodu
Date: June 18, 2025
__________________________________________________________________________________
Instructions:

1) Write a program that stores the following amino acids into an array:

Trp
Arg
Liu
Ilu
Asp

Then prompt the user to give you a three letter amino acid abbreviation.
Test to see if the a.a. the user gave you is in the array or not.
If it is, print out a message to the user saying "Amino acid found",
otherwise print out "Amino acid NOT found".
You have to use a loop structure to look up
every element in the array (one by one) and compare it with what the user gave you.

'''

#Biggest issue: ensuring the array and user input are both lowercase before comparsion
import numpy as np

#store amino acids in array
aacid  = np.char.lower(['Trp', 'Arg', 'Liu', 'Ilu', 'Asp'])
uin = input("Guess the three letter abbreviation of amino acids:").lower()


for amino in aacid:    
    if uin == amino:
        print(" Amino acid found ")
        break
else:
    print("Amino acid NOT found. Try again!")
       
            
        
            
    





