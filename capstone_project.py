#GROUP PROJECT - draft
#Get user to input a file, check for FASTA format.
import re
import os

#file_reader author Faith Igomodu, minor clean-up by Solenn Orozco
#define a function to check if the file is in FASTA format, and the separate each sequence block into a directory (header, sequence)
def file_reader(filename):
    seq_pattern = r">([^\n]+)\n([A-Za-z\n]+)(?=>|$)" #define sequence blocks of header and sequence for regex
    fasta_dict = {} #create a dictionary for the sequences in the file
    #Check if file exists
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    #After checking that the file exists, open it to fill up the dictionary
    with open(filename, "r") as file:
        seq_fasta = file.read().strip()
        if not seq_fasta.startswith(">"): #Check for FASTA format
            raise ValueError("The file does not appear to be in FASTA format.")
        #Find all of the header:sequence blocks to separate into two groups, case insensitive
        seq_matches = re.finditer(seq_pattern, seq_fasta, flags=re.IGNORECASE)
        for match in seq_matches: #Fill up the dictionary
            header = match.group(1).strip()
            sequence = match.group(2).replace("\n", "").strip()
            fasta_dict[header]= sequence # Dictionary with header as key and sequence as value
            
    return fasta_dict  # Return the first sequence block found

#orf_finder co-authors Solenn Orozco and Theresa Miller
#define a function to find n ORFs (based on user input from main function)
#in forward sequence starting at positions 1, 2, then 3 and then backwards at positions 4, 5, 6 
def orf_finder (header, seq, frame, position, min_orf):
    #define start codon
    start_codon = "ATG"
    #define stop codons
    stop_codon = {"TAA", "TAG", "TGA"}
    #create useful variables
    orf_count = 0 #to count orf and make sure it is within the minimum
    in_orf = False
    orf_for_frame = ""
    orf = ""
    while position < len(seq) -2:
        #Go through the sequence 3 bases at a time with starting position defined by frame in frame_orf function
        bases = seq[position:position+3]
        if bases == start_codon and not in_orf: #checks that in_orf is false to avoid bugs from starting codon recording while one is running
            in_orf = True #flags the loop as 'in-orf' after start codon has been found
            orf += bases #adds the 3-bases (start codon) to the current orf
            #adjust position based on frame
            if frame <4:
                orf_pos = position + 1
            elif frame >3:
                orf_pos = -position-1
        elif bases in stop_codon and in_orf:
            orf += bases #add stop codon at the end of the orf
            in_orf = False #flag that the orf has been found in its entirety
            if len(orf) >= min_orf: #Check that the length meets the minimum length requirement
                #format the orf in codon size 3, max of 15 per line
                codons = [orf[i:i+3] for i in range(0, len(orf),3)]
                codon_lines = [' '.join(codons[i:i+15]) for i in range (0, len(codons), 15)]
                codon_final_form = '\n'.join(codon_lines)
                #Current orf with the header info
                orf_for_frame += f"{header} | FRAME: {frame} | POS: {orf_pos} | LEN: {len(orf)}\n{codon_final_form}\n"
            orf = "" #empty out for next orf
        elif in_orf:
            orf += bases #add on the 3-bases to the orf while in_orf = True
        position += 3
    if orf_for_frame:
        print(orf_for_frame.strip()) #print out the last orf found with its header, then back to the loop we go

#frame_orf co-authors Solenn Orozco and Theresa Miller
def frame_orf (fasta_dict, min_orf):
    #Go through each item in the dictionary
    for header, sequence in fasta_dict.items():
        #frames 1-6
        for frame in range(1,7):
            #for frames 1-3, define position and get ORFs using orf_finder
            if frame <4:
                position = frame -1
                orf_finder(header, sequence, frame, position, min_orf)
            #for frames 4-6, define position, get reverse complement sequence, and get ORFs using orf_finder
            elif frame >3:
                position = frame -4
                #define the complements of each base
                complement_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
                #get complement of sequence
                seq_comp = ''.join(complement_dict.get(base, base) for base in sequence)
                #get reverse of complement sequence
                seq = seq_comp[::-1]
                #use orf_finder with the reverse complement sequence and adjusted position
                orf_finder(header, seq, frame, position, min_orf)

#main program author Faith Igomodu with minor clean-up by Solenn Orozco     
def main():
    #Ask user for file name, then run file_reader to check if the file meets requirements and to create a sequence dictionary if it does.
    filename = input("Enter the file name of a FASTA file: ")
    fasta_dict = file_reader(filename)
    #Ask the user for the minimum ORF to search for.
    orf_count_choice = input("Would you like to define the number of ORF to search for? Default is 50 (Y/N): ")
    #Pester user until a correct input is given
    while orf_count_choice not in ('Y', 'N'):
        orf_count_choice = input("Invalid entry, please type 'Y' or 'N': ")
    if orf_count_choice == 'Y':
        min_orf = int(input("Please enter the minimum length of ORF to search for: "))
    #Define default
    elif orf_count_choice == 'N':
        min_orf = 50
    #Run user file and min_orf with frame_orf
    frame_orf(fasta_dict, min_orf)

main()
