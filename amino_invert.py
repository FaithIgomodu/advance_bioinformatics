'''
Author:     Faith Igomodu
Date:       June 14, 2025
___________________________________________________________________________________________
Instructions:
Create an inversion: get two positions in the sequence from the user and invert the 
sequence of the amino acids between them. For example, if the user enters 3 and then 
6, the program should replace Asn, Gln, His, Leu with Leu, His, Gln, Asn. Print the array 
before and after the inversion.

'''
#store amino acid in dictionary
poly_dict = {1: "Phe",
             2: 'Val',
             3: 'Asn',
             4: 'Gln',
             5: 'His',
             6: 'Leu',
             7: 'Cys',
             8: 'Gly',
             9: 'Ser',
             10:'His' }

#extracted keys 
keys_key = []

#exracted values 
values_inv = []

#show user the original dict of amino acids
print("\n\nThe amino acid dictionary before inversion:", poly_dict)

#get value 1
key_one = int(input("Enter a number between 1 and 10:"))

#get value 2 
key_two = int(input("\nEnter a another number between 1 and 10:"))

#gather keys to be inverted 
for val_one in poly_dict:
    if key_one >= val_one and key_two <= val_one:
     keys_key.append(val_one)   

#gather values to be inverted
for val_in in keys_key:
    values_inv.append(poly_dict[val_in])

#reverse extracted values
val_reverse = values_inv[::-1]


#update dictionary
for k in range(len(keys_key)):
    key = keys_key[k]
    poly_dict[key] = val_reverse[k]

print("\n\nThe new amino acid dictionary after inversion:", poly_dict)