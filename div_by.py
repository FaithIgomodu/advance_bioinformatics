'''
Author      : Faith Igomodu
Date        : June 24, 2025
Professor   : Ana Belle 
'''

def div_by(n ,d):
    '''
    Divides two ints returns true/false.

    Args:
    ----

    n = int > 0
    d = int > 0


    Returns:
    -------
    True if d divdes evenly
    False if it does not 


    '''


    if n%d == 0:
        return True
    else:
        return False


print(div_by(10,3))
print(div_by(195,13))