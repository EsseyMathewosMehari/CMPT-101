#---------------------------------
# Name:Essey Mehari
# Program: L3Q1EM.py
#----------------------------------
#I certify that this work is mine
#----------------------------------
#Purpose: To get user input and display infromation 
#----------------------------------

#the purpose of this function is to get a user to input a string and then use a while loop to check if 
#it is more than or equal to 8 charaters and ends with a '?'
def get_string():
    string = input('\nEnter 8 or more characters endiing with a question mark:' '\n \t ')
    while len(string) <8 or string[-1] != '?':
        string = input('\tIncorrect - try again: ') 
    return string

# Prints out the ogirinal string, determins and outputs the : string lentgh, second char,
#second last char, and it will switch the first 3 chars and the last 3 chars
def explore_chars(string):
    print('')
    word = len(string)
    print('(a) Length --------> ', word, 'chars')
    print('(b) 3rd char ------> ', string[2])
    if string[-3].isupper():
        print('(c) 3rd last ------> ', string[-3], '(NOT lowercase)')
    else:
        print('(c) 3rd last ------> ', string[-3], '(lowercase)')
    print('(d) Original ------> ', string)
    print('(e) Swap 4 chars -->' ,string[(4):(word)],string[4:(word-4)], string[0:4], end = "")
    print('')
    

#Count how many uppercases there are and display the quantity and the
#letters themselves
def count_uppercase(string):
    i = 0
    letter =''
    for upper in string:
        if upper.isupper():
            i += 1
            letter += upper
    print('(f) Uppercase amt ->',i, '('+ letter+ ')')
    

#Main function that calls upon the three strings
def examine_string():    
    string = get_string()
    explore_chars(string)
    count_uppercase(string)

#calling the main function    
examine_string()