#---------------------------------
# Name:Essey Mehari
# Program: L3Q1EM.py
#----------------------------------
#I certify that this work is mine
#----------------------------------
#Purpose: 
#----------------------------------

print('\nMacewan Event Booking')
venue= input('\n1. Select venue:(P)ool, (g)ym, or (c)lassroom (P, G, or C)?  :')
if venue.lower() == 'p':
    total= int(75)
    print('The pool is $75/hr')
    hours= int(input('\n2. Enter hours requested (number): '))
    if hours < 3:
        print(hours,'hour(s) changed to 3 hours daily min')
        hours= 3
    elif hours> 10:
        print(hours,'hour(s) changed to 10 hours daily max')
        hours= 10
    day= input("\n3. Enter day requested (ie Monday, Tuesday..): ")
    print("\nBooking", hours ,"hours at $", total, ' costs $',total * hours)
    if day.lower()=="monday" or day.lower()== "tuesday" or day.lower()== "wednesday"or day.lower() == "thursday":
        print('A 30% discount is a saving of $', (total*hours*.3))
        print('The overall cost is $', (total * hours)-(total*hours*.3))
    elif day.lower()== "friday":
        print('A 10% discount is a saving of $', (total*hours*.1))
        print('The overall cost is $', (total * hours)-(total*hours*.1))        
    elif day.lower()== "saturday" or day.lower()== "sunday":
        upgrade= input('\nIf upgraded to 20hrs, you will get a 20% disscount otherwise 0%.\nwould you like to upgrade? (Yes or No): ')
        if upgrade.lower() == 'yes':
            print("\nBooking 20 hours at $", total, ' costs $',total * 20)                        
            print("A 20% discount is a saving of", (total*hours*.2))
            print('The overall cost is $', (total * hours)-(total*hours*.2))
        elif upgrade.lower== "no": 
            print("\nA 0% discount is a saving of $0") 
            print('The overall cost is $', (total * hours))
elif venue.lower() == 'g':
    print('The gym is $50/hr')
    total= int(50)
    hours= int(input('\n2. Enter hours requested (number): '))
    if hours < 3:
        print(hours,'hour(s) changed to 3 hours daily min')
        hours= 3
    elif hours> 10:
        print(hours,'hour(s) changed to 10 hours daily max')
        hours= 10
    day= input("\n3. Enter day requested (ie Monday, Tuesday..): ")
    print("\nBooking", hours ,"hours at", total, '$ costs $',total * hours)
    if day.lower()=="monday" or day.lower()== "tuesday" or day.lower()== "wednesday"or day.lower() == "thursday":
        print('A 30% discount is a saving of $', (total*hours*.3))
        print('The overall cost is $', (total * hours)-(total*hours*.3))
    elif day.lower()== "friday":
        print('A 10% discount is a saving of $', (total*hours*.1))
        print('The overall cost is $', (total * hours)-(total*hours*.1))        
    elif day.lower()== "saturday" or day.lower()== "sunday":
        upgrade= input('\nIf upgraded to 20hrs, you will get a 20% disscount otherwise 0%.\nwould you like to upgrade? (Yes or No): ')
        if upgrade.lower() == 'yes':
            print("\nBooking", hours ,"hours at $", total, 'costs $',total * 20)            
            print("A 20% discount is a saving of", (total*20*.2))
            print('The overall cost is $', (total * hours)-(total*20*.2))
        elif upgrade.lower()== "no":
            print("\nBooking", hours ,"hours at $", total, ' costs $',total * hours)            
            print("A 0% discount is a saving of $0") 
            print('The overall cost is $', (total * hours))
elif venue.lower() == 'c':
    amt= input('\tAmt of seats: (A) 100+, (B) 50-99, or (C)under 50 (A, B, C)?:')
    if amt.lower()=="a":
        seat=(100)
        print('A 100+ seat classrom is $100/hr')
    elif amt.lower()=="b":
        seat=(65)
        print('A 50-99, seat classrom is $65/hr')
    elif amt.lower()=="c":
        seat=(30)
        print('A under 50, seat classrom is $30/hr')
    hours= int(input('\n2. Enter hours requested (number): '))
    if hours < 3:
        print(hours,'hour(s) changed to 3 hours daily min')
        hours= 3
    elif hours> 10:
        print(hours,'hour(s) changed to 10 hours daily max')
        hours= 10
    day= input("\n3. Enter day requested (ie Monday, Tuesday..): ")
    print("\nBooking", hours ,"hours at $", seat, ' costs $',seat * hours)
    if day.lower()=="monday" or day.lower()== "tuesday" or day.lower()== "wednesday"or day.lower() == "thursday":
        print('A 30% discount is a saving of $', (seat*hours*.3))
        print('The overall cost is $', (seat * hours)-(seat*hours*.3))
    elif day.lower()== "friday":
            print('A 10% discount is a saving of $', (seat*hours*.1))
            print('The overall cost is $', (seat * hours)-(seat*hours*.1))        
    elif day.lower()== "saturday" or day.lower()== "sunday":
        upgrade= input('\nIf upgraded to 20hrs, you will get a 20% disscount otherwise 0%.\nwould you like to upgrade? (Yes or No): ')
        if upgrade.lower() == 'yes':
            print("\nBooking 20 hours at $", seat, ' costs $',seat * 20)            
            print("A 20% discount is a saving of $", (seat*20*.2))
            print('The overall cost is $', (seat * 20)-(seat*20*.2))
        elif upgrade.lower()== "no":
            print("\nBooking", hours ,"hours at $", seat, ' costs $',seat * hours)            
            print("A 0% discount is a saving of $0") 
            print('The overall cost is $', (seat * hours))