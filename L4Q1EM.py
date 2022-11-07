#---------------------------------
# Name:Essey Mehari
# Program: L3Q1EM.py
#----------------------------------
#I certify that this work is mine
#----------------------------------
#Purpose: To Write a program that displays ascending/decending numbers based on input
#----------------------------------

step= int(input('Enter a number (1 to 10): '))

while ((step>10) or (step<0)):
    print('Error!')
    step= int(input('Enter a number (1 to 10): '))

count=input('Count up or down (U or D): ')    
while not ((count.upper()=='U') or (count.upper()=='D')):
    print('Error!')
    count= input('Count up or down (U or D): ')
if count.upper()=='U':    
    step1= (step*-5)+1
    step2 = step1
    o= int(0)
    while o<5:
        step2+= step
        o+=1
    for i in range(step1,step2,step):
        print(i, end=' ')
    print('_ ', end = "")
        
    
elif count.upper()=='D':
    step1= (step*5)+1
    step2 = step1
    o= int(0)
    while o<5:
        step2-=step
        o+=1
    for i in range(step1,step2,-step):
        print(i, end=' ')
    print('_ ', end = "")
    
    step3 = step1 - (step * 6)
    step4 = step1 - (step * 11)
    
    for i in range(step3,step4,-step):
            print(i, end=' ')
            
reveal=input('\nShow answer (y or n): ')
if (reveal.upper()=='Y'):
    print('Answer: 1')
elif (reveal.upper()=='N'):
    print('Program ended')
    
