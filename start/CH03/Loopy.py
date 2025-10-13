#!/usr/bin/env python3
# example workign with Loops
#By Margaret

question = input("Is today a good day? Please answer with y or n:")

if question == 'y':
    #Create a loop of 10 times saying yea it is"
    number = 1 
    while number < 11:
        print("yes it is")
        number += 1
elif question == 'n':
    print('Thats okay, tomorrow will be ')
elif question == 'idk':
    print('thats okay')
else:
    print('Please enter a valid input pf y or n for yes or no')
