'''
Author: Faith Igomodu
Date: June 18, 2025
__________________________________________________________________________________
Instructions:
Modify the question from the pervious week
(where you were asked to store your name in a variable and have
the user guess it), so that you keep on asking the user for names till he\she gets it right! So
he\she has to guess your name right BEFORE you exit the program. Use a while loop.

'''
#store name in variable 
nam = "faith"
user_in = ''


while user_in != nam.lower():
    #prompt user for input
    user_in = input("Guess my name:").lower()
    if user_in == nam.lower():
        print("Well done, you guessed correctly")
    else:
        print("You're guess is wrong, try again")

    
