'''
Author: Faith Igomodu
Date: July 10, 2025
Course: Advance Bioinformatics
09.02
_________________________________________________________________________________________________________
Instructions:
Write a program that ask the user for a DNA sequence,
the program should then return the protein sequence that corresponds to that DNA.
You can assume here that the DNA sequence that is given by the user contains multiples of 3 nucleotides,
and that the protein is in frame 1 of the sequence. 

'''

def protein_translate(dna):
    '''
    Function translates users input into amino acids using a codon-to-amino dictionary. 


    Args:
    dna: A DNA sequence (e.g., "ATGC")

    Return:
    str: the translated protein sequence. 


    '''
    #translation dictionary is made of keys (codons) and values ( amino acids).
    #this table is used to translate user input to corresponding protein sequence 
    translation_dict = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}



    last_codon_start = len(dna) - 2 
  
    #initializes an empty string to store the translated protein sequence 
    protein = ""
       
    #iterate over protein sequences in steps of 3 
    for base in range(0, last_codon_start,3):
        #extracts current codon start at index base using string slicing.
        codon = dna[base:base+3]
        #use dna sequence to find corresponding codon in gencode dictionary. 
        amino_acid = translation_dict.get(codon.upper(), 'X')
        protein = protein + amino_acid 
    return protein 
        




if __name__ == "__main__":
    #inform user the type of application 
    print("---- Protein Translation Application----")
    #obtain user input 
    user_input = input("\nEnter gene sequence (3 bases) to be translated: ")
    #translate user dna sequence to amino acid 
    translate = protein_translate(user_input)
    print(f"DNA: {user_input} --> Protein: {translate}")




