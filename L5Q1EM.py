#---------------------------------
# Name:Essey Mehari
# Program: L5Q1EM.py
#----------------------------------
#I certify that this work is mine
#----------------------------------
#Purpose: 
#----------------------------------

def draw_edges(symbol, amt):
    print(symbol + "" * (amt-2) + symbol)
    
def draw_top(symbol, size):
    print('\n', end="")
    print(""+ symbol*(int(size)-2)+ "", end="")
    
def draw_column(amt_space,symbol, amt_rows):
    i=1
    while (i<(amt_rows)-2):
        print(" "*(amt_space//2-1), symbol)
        i+= 1
        if (i ==amt_rows -2):
            print(symbol + " " *(amt_space//2 -2), symbol)

def draw_bottom(symbol, amt_symbol):
    print(" "+symbol*((amt_symbol//2)-1))
       
def get_size(size):
    size= input('Enter an odd number 5 or greater: ')
    while int(size) % 2 == 0 or int(size)<5:
        size= input('Enter an odd number 5 or greater: ')
    return size

def draw_J(symbol):
    size=get_size(1)    
    symbol = input('Enter symbol: ')
    draw_top(symbol, int(size))
    draw_edges(symbol,int(size))
    draw_column(int(size),symbol, int(size))
    draw_bottom(symbol, int(size))

draw_J('*')

