'''
Author: Faith Igomodu
Date: June 25, 2025
Description: A function that asks user for a file name, prints filename if found

'''

def file_search():
    '''
    A function that asks user for filename five times and prints it if found


    arg:
    ----
    mone, user inputs filename


    return:
    --------
    none, results will be printed to std.output

    '''

    iteration = 5
    for num in range(iteration):
        user_input = input(f"Enter the name of a file: (Attempt {num + 1}/{iteration}): ")
        if user_input == 'seq_file':
            print("File found")
        else:
            print("File name not valid")
   






file_search()
