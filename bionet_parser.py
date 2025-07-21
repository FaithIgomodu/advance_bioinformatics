'''
Author: Faith Igomodu
Course: Advance Bioinformatics
Date: July 15, 2025
Assignment : Week 10
Instructions: 

Write a program that parses out the Bionet file. And stores the enzyme name and cut site in a dictionary.
For the dictionary to be useful later, we need to convert thecut site into a regular expression and store
that as the value for each dictionary entry.The key will be the enzyme name.


Solution stratgey
read file and store in variable 
discard header
discard blank lines
split enzyme and recognition sites
convert recognition site into regular expression
store in a dictionary



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''

import re

bio_dict = {}

def bionet_parse(filename):
    '''
    Function parse bionet file, stores enzyme and restriction site in a dictionary.

    arg:
    filename: a bionet file


    return:
    dictionary: of enyzmes and restriction sites


    '''

    global bio_dict

    #regular expression to remove header and blank lines
    header = re.compile(r'^\s*(REBASE\b.*|.*(RICH|Roberts)\b.*|\s*Copyright.*|\s*Rich Roberts.*|\s*$)',re.IGNORECASE)
    
    #open file 
    with open(filename, 'r') as bio:
        for base in bio:
            line = base.strip()
            if not header.match(line):
                enzyme = re.split(r'\s{2,}', line)
                if len(enzyme) >= 2:
                    seq = enzyme[1].strip()
                    enz = enzyme[0].strip()
                    bio_dict[enz] = seq


    return bio_dict


def print_bio(filename):
    '''
    Function prints the contents of a parsed Bionet file

    args:
    filename: parsed bionet file

    return:
    none
    '''
    print("\nBionet File Parser \n\n(Enzyme Name: Cut Site )")    
    for enz, seq in bio_dict.items():
        print(f"{enz} ------------------- {seq}")
        
        
if __name__ == '__main__':
    
    file = input("Enter the name of Bionet file:")
    bio_file = bionet_parse(file)
    print_bio(bio_file)

