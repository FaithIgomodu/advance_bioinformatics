'''
Author: Faith Igomodu
Date: May 30, 2025
Description: calculates the GC and AT contents of a sequenced obtained from a user
'''

#variable definition
gc_count = 0
at_count = 0


dna_seq = input("Enter DNA sequences with a space in between each:").split()
for nucleotide in dna_seq:
    nu_len = len(nucleotide)
    
    gc_count = nucleotide.count("G") + nucleotide.count("C")
    at_count = nucleotide.count("A") + nucleotide.count("T")
    
    gc_per = (gc_count*100)/nu_len
    at_per = (at_count*100)/nu_len

print(f"The GC content of the DNA sequence'{nucleotide}'given is: {gc_per:.1f}%")
print(f"The AT content of the DNA sequence'{nucleotide}'given is: {at_per:.1f}%")





