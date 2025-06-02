#Author: Faith Igomodu
#Date: may 30, 2025
#Description: obtain multiple file names from user, read contents and print to standard output


#prompt user for file name
file_name= input("Enter file names with a space in between:").split()


#Use loop to iterate over file contents, store in variable text, and print to std.output
for line in file_name:
    with open(line, 'r') as letters:
        text = letters.read()
        print(f"file'{line}' contains:\n {text}\n")

        
