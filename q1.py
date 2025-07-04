'''
Author: Faith Igomodu
Date: June 3, 2025
Instructions:



1) Attached is a file called genomic_dna.txt. It contains a DNA sequence that is comprised of two 
exons and an intron. The first exon runs from the start of the sequence to the 63 bp, and the 
second exon runs from the 91 bp to the end of the sequence. Write a program that will print out 
to files the coding and non-coding regions of the sequence (i.e. The exons in one file called 
coding.txt, and the intron into another file called non_coding.txt).
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''
#1)


#open and read file, store in variable
with open ("genomic_dna.txt", "r" ) as seq_file:
    sequences = seq_file.read()
    seq_len = len(sequences)
    #print(f"The file genomic_dna.txt contains: {sequences}, with length of {seq_len}")

#extract exons and introns
exon_one = sequences[:63]
exon_two = sequences[90:]
intron   = sequences[63:90]
exons    = exon_one + exon_two
#print('The length of exons are: ', len(exons), 'the length of the introns are: ', len(intron))



#write exons to file
with open ('coding.txt', 'w') as code:
    code.write(exons + "\n")

#write introns to file
with open ('non_coding.txt', 'w') as noncode:
    noncode.write(intron + "\n")
