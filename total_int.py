'''
Author: Faith Igomodu
Date: June 1, 2025
Course: DBST 651 
Descriptino: program will accept five int from user and caluclate mean and sum. Results wil be printed to std.output.
_______________________________________________________________________________________________________________________

Ask a user for 5 number. Use the input function, and store each number in a variable.
Then calculate the sum and average of the numbers. Print out both the sum and average to the screen.
'''

'''

pseudocode

prompt user for five numbers separated by a space
convert input string to int
store value in a variable
calculate sum and mean of list
print results to std.output
'''

#prompt user for five numbers 
num_string = input("Enter 5 integers with a space in between").split()


#convert strings to int
for index in range(len(num_string)):
    num_string[index] =int(num_string[index])
      
#store each number into a variable
a_int, b_int , c_int , d_int , e_int = num_string

#calculate sum and mean

total = sum(num_string)
avg = total/ len(num_string)

print(f"The sum of all integers entered is: {total} and the mean is: {avg}")
