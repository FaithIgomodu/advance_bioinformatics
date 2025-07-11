'''
Author: Faith Igomodu
Date: July 1 , 2025 
Course: Advance Bioinformatics
Discussion_02
Instructions:
Write a program that produces the following output when
searching for the word RNA in the paragraph : 

Output:

(RNAi) ends at position 49

(dsRNA) ends at position 211

(ssRNAs) ends at position 374

mRNAs. ends at position 431
_____________________________________________________________________________
'''

import re

def word_search(word):
    '''

    The function searches for RNA's in a string 
    and prints its location when found.

    arg:
    ----
    string array


    return:
    ------
    
    '''   

   
    text = word.strip()     
    pattern = re.compile(r"\(RNAi\)|\(dsRNA\)|\(ssRNAs\)|mRNAs\.")        
    matches = pattern.finditer(text)
    for match in matches:
        print(match.group(), 'ends at position', match.end())


#function call
lines ="""Several rapidly developing RNA interference (RNAi)
methodologies hold the promise to selectively inhibit gene expression in
mammals.RNAi is an innate cellular process activated when a
double-stranded RNA (dsRNA) molecule of greater than 19 duplex
nucleotides enters the cell, causing the degradation of not only the
invading dsRNA molecule, but also single-stranded (ssRNAs) RNAs of
identical sequences, including endogenous mRNAs."""

word_search(lines)


