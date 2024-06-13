import random
peoples=['A','B','C','D','E']
random_=random.randint(0,4)
if random_==0:
    print('{} is going to buy the meal today!'.format(peoples[0]))
elif random_==1:
    print('{} is going to buy the meal today!'.format(peoples[1]))
elif random_==2:
    print('{} is going to buy the meal today!'.format(peoples[2]))
elif random_==3:
    print('{} is going to buy the meal today!'.format(peoples[3]))
else:
    print('{} is going to buy the meal today!'.format(peoples[4]))
#
#Or import random
#random_=random.randint(0,4)
#print('{} is going to buy the meal today!'.format(names[random_]))