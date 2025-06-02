#Author: Faith Igomodu
#Date: May 30, 2025
#Description: obtain file name from user, read contents and save to a new file 



# Prompt user for file names
file_names = input("Enter file names with a space in between: ").split()

# first open new file
with open("new_seq_file.txt", 'w') as new_seq_file:
 # Loop through each file user entered
    for line in file_names:
        #read each file 
        with open(line, 'r') as letter:
            text = letter.read()
            new_seq_file.write(text + '\n')
