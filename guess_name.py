'''
Author: Faith Igomodu
Date: 6/15/2025
Instructions:
your name in a variable. Then ask the user to guess your name
If he\she guesses right, display the message "Well done,
good guess work!", otherwise display the message "Try again next time!"
and just exit the program at that point.

___________________________________________________________________________
Pseudocode 
store name in a variable
prompt user to guess you're name
use equality operator to see if guess is accurate
if not exit program
'''

#store name in variable
m_name = 'faith'

#prompt user for input
user_in = input("Guess my name:").lower()

#use if else statement to check if guess if correct
if user_in == m_name.lower():
    print("Well done, you guessed correctly")

else:
    print("You're guess is wrong, try again")
