#Author: Faith Igomodu
#Date: May 30, 2025
#Description: Read files located in a directory, save contents to another file  called output.txt



#import modules
import os


#First get the current working directory
current_wd = os.getcwd()

#Then print working directory to screen to confirm
print("Current working directory is:", current_wd)

#file path
file_dir = os.path.expanduser("~/Downloads/BIFS617/03/week_03")

#Print path where files are
print("Files are located here: ", file_dir)

#List of files in path 
file_names = os.listdir(file_dir)

#Print list of files in directory 
print(file_names)

#Inform user file in located in current directory
print("Output.txt is located in:", current_wd)

#open new file, use for loop to read file save contents in variable text,  and write to new file. 

with open("Output.txt", 'w') as new_output_file:
    for files in file_names:
        file_path= os.path.join(file_dir , files)
        with open(file_path, 'r') as letter:
            text=letter.read()
            new_output_file.write(text + '\n||\n')
