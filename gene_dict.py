'''
Author: Faith Igomodu
Date: July 10, 2025
Course: Advance Bioinformatics
09.01
___________________________________________________________________________________________
Instructions: 
Write a program that asks a user for a gene ID or
accession number and returns the sequence that corresponds to that gene.
Use a dictionary to accomplish this. Get the genes and their sequences
from NCBI and create the dictionary so that the key = gene ID and value = sequence.
Handle the case where the gene ID is not found in the dictionary. 
'''


def gene_id(acc):
    '''

    Retrieves a DNA sequence based on a given accession number

    Args:
    acc: accession number of DNA sequence


    return:
    seq: the sequence that corresponds to the accession number


    '''


    # Dictionary mapping accession numbers to their respective DNA sequences.
    # Note: Sequences are shortened for demonstration purposes.
    accession_seq = {
    'NR_077053.1': 'GTTAAGTGACTAAGCGTACAAGGTGGATGCCTTGGCAATCA',
    'OR678186.1': 'AGTTCCGACCTGCACGAATGGCATAATGATGGCCAGGCTGTCTCCACCCGAGAC',
    'OR678180.1': 'AGTTCCGACCTGCACGAATGGCATAATGATGGCCAGGCTGTCTCC'
     }

    if acc in accession_seq:
        return accession_seq[acc]
    else:
        return none 

    





if __name__ == '__main__':

    uin = input("\nEnter the accession number of sequence:")
    accession = gene_id(uin)
    print(f"\nThe accession number {uin} corresponding sequence is: {accession}")
