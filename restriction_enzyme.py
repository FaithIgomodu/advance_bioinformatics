'''
Author: Faith Igomodu
Course: Advance Bioinformatics
Date: July 15, 2025
Assignment: week 10
Instructions: 

Download the attached sequence file, it contains a DNA sequence in FASTA format.
Write a program that finds the fragment lengths that would be generated (if any)
if the enzyme AbcI is used. That enzyme’s cut site is ANT^AAT. Where ^ denotes where the enzyme will cut.
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
#regular expression module
import re

def enzyme(seq):
    '''
    Function uses regular expression to find  restriction enzyme site. 


    args:
    seq: FASTA file of DNA sequences. 

    return:
    enzyme: an array of restriction enzyme site. 
    
    '''

    #array of enzyme 
    enzyme = []

    #open and read FASTA file
    with open(seq, 'r') as File:
        #store sequence in variable fasta 
        fasta = File.read()  
        #re expression to find restriction sites             
        pattern = re.compile(r'A[GATC]AAT', re.IGNORECASE)
        matches = pattern.finditer(fasta)
        for match in matches:
            enzyme.append(match.group())
                
    return enzyme 
            
            
if __name__ == '__main__':
        app = input('--------Restriction Enzyme Site Search App-----------')
        file = input("Enter file name (include extension):")
        re_site = enzyme(file)
        sites = input(f"The restriction enzyme sites are: {','.join(re_site)}")
        print(sites)
    

    
