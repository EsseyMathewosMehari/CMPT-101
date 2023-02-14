#---------------------------------
# Name:Essey Mehari
# Program: L2Q1EM.py
#----------------------------------
#I certify that this work is mine
#----------------------------------
#Purpose: Prograqm for user input, convert string to int, and and make a story with the data collected
#----------------------------------
print("\nPlease enter the following:")
name= input("\t(1) a person: ")
car= input("\t(2) a vehicle: ") 
numb= input("\t(3) a number: ") 
occ= input("\t(4) an occupation: ") 
hob= input("\t(5) a hobby: ") 
print('\nHere is a story using your words:')
print('\nDid you know that (1) ' + name+ ' drives a/an (2) '+car+'? ')
print('The license plate number is ' + str(int(numb)**2) + ' which is (3) '+ numb+' squared.')
print("If I were a (4) "+occ+", I would change my license plate number")
print('to '+numb+numb+numb+" and I'd spend my free time (5) "+hob+".")