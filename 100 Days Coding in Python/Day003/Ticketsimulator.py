print('Welcome to the Rollercoaster!!')
height=float(input('What is your height in cm?\n'))
bill=0
if height>=120:
    print('Congratulations, you can ride the rollercoaster!')
    age=int(input('How old are you?\n'))
    if age<12:                                      #Need to be true to goes on.  
        bill=5
        print('Child tickets are $5')
    elif 12<=age<=18:                               #Need to be true to goes on.
        bill=7
        print('Teenager tickets are $7')
    elif age>=45 and age<=55:
        print('Everything is going to be okay. You can have a free ride!')    
    else:                                           #Need to be false to goes on.
        bill=12
        print('Adult tickets are $12.')
    photo=input('Would you like to take a photo at the rollercoaster? [Y/N]\n').upper()[0]
    if photo=='Y':
        print('Nice, you must pay ${}.'.format(bill+3))
    else:
        print('All right, so you must pay ${}'.format(bill))

else:
    print("Unfortunately, you can't ride the rollercoaster.")