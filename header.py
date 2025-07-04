'''
Author: Faith Igomodu
Date: July 1 , 2025 
Course: Advance Bioinformatics
Discussion_01
Instructions:
Write a program that uses a regular expression to extracts out and prints
to the screen the accession number of a sequence in a FASTA file.
_____________________________________________________________________________
'''

import re 

def header():
    '''
    Function extracts accession number of a sequence in FASTA FILE

    args:
    -----
    none , user input is obtained


    return:
    ------
    matches found 


    
    '''
    #obtain name of file
    user_input = input("Enter the name of the FASTA file:")

    #read file 
    with open(user_input, "r") as seq:
        #regular expression object
        pattern = re.compile(r'^>\s*(\S+)')
        #loop through file 
        for lines in seq:
            #store matches in variable 
            matches = pattern.finditer(lines)
            #loop through match and return 
            for match in matches:
                return match.group(1)          
    


#function call

print("The accession number for FASTA file is: ", header())

