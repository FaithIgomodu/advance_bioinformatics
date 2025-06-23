'''
Author: Faith Igomodu
Date: June 18, 2025
__________________________________________________________________________________
Instructions:
Write a program that asks the user for 5 numbers,
using a for loop and one input function call inside that for loop. Sum the numbers as you are getting
them from the user, then display the sum and average to the user at the end.

'''
nums =[]

#prompt user for five numbers
for _ in range(5):
    user_input = int(input("Enter A number: "))
    nums.append(user_input)

total = sum(nums)
avg   = total/5
print(f"The sum of the 5 numbers is: {total}, The average of the numbers is: {avg}")
