
'''
Author: Faith Igomodu
Course: Advamce Bioinformatics
Assignment: Parse GenBank Files 

'''



def GenBank_reader(filename):
    '''
    Read GenBank file extracts accession number and protein sequencs and stores in a dictionary. 

    '''
    #import regexpression module 
    import re
    #variable defition 
    genbank_dict = {}


    #open file 
    with open (filename, "r") as file:
        #read file 
        genfile = file.read()
        #regular expression for extracting accession number and protein sequences 
        matches = re.finditer(r"ACCESSION\s+(\w+).*?ORIGIN\s+([\s\da-z]+)//",genfile, re.DOTALL | re.IGNORECASE)
        #extract accession number and protein sequence 
        for match in matches: 
            accession = match.group(1).strip()
            protein = re.sub(r"[\d\s]", "", match.group(2)).upper()
            #store accession number and protein sequence in dictionary 
            genbank_dict[accession] = protein
            
    return genbank_dict




if __name__ == '__main__':
    print('----GenBank File Parser----')
    filename = input('Enter the name of a GenBank File:')
    parse_file = GenBank_reader(filename)
    for key, value in parse_file.items():
        print(f"\n\nThe Accession Number is: {key}:\n\n The Protein sequence is {value}")
    
    


