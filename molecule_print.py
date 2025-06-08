'''
Author: Faith Igomodu
Date: June 1, 2025
Description: program will store molecules in an array and print the 3rd, and 5th  to std.output
______________________________________________________________________________________________________________

'''
import numpy as np

'''

pseudocode

store molecules in an array
store third element in variable
store fifth element in variable
print third and fifth element to the std.output

'''


molecule_arr = np.array(["peroxidase","gene", "protein", "oxidase", "hemoglobin"])

third_mole = molecule_arr[2]

fifth_mole = molecule_arr[4]


print(f"The third molecule in the array is {third_mole} \n\n\n The fifth molecule is {fifth_mole}")





