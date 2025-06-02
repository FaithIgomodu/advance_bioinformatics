'''
Author: Faith Igomodu
Date: May 30, 2025
Description : obtain DNA sequence from user and transcribe to RNA 
'''


dna_seq = input("Enter DNA sequences with a space in between each:").split()


#Use loop to iterate over file contents, store in variable text, and print to std.output
for nucleotide in dna_seq:
        seq = nucleotide
        rna = seq.replace("T","U",)
        print(f"The DNA sequence'{nucleotide}' transcribed to RNA  is: {rna}")

