name1=input('What is your name?\n').upper().strip()
name2=input('What is your name?\n').upper().strip()
T=(name1+name2).count('T')
R=(name1+name2).count('R') 
U=(name1+name2).count('U')
E=(name1+name2).count('E')
L=(name1+name2).count('L')
O=(name1+name2).count('O')
V=(name1+name2).count('V')
E1=(name1+name2).count('E')
c1=T+R+U+E
c2=L+O+V+E1
score=int(f'{c1}{c2}')
if score<10 or score>90:
    print('Your score is {}, you go together like coke and mentos.'.format(score))
elif 50>score>40:
    print('Your score is {}, you are alright together.'.format(score))
else:
    print('Your score is {}.'.format(score))