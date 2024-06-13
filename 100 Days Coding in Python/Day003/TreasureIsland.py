print('Welcome to the Treasure Island.\nYour mission is to find the Treasure.')
lr=input('You are inside the castle and need to choose a door: Left or Right?\n').upper().strip()[0]
if lr=='L':
    print('Well done, you made it to level 2.\nYou fall at the beach and need to go to the Island.')
    sw=input('Now,you choose to: Wait or Swim?\n').upper().strip()[0]
    if sw=='W':
        print('Congratulations,you made it to level 3.\nTo find the treasure you need to open a door.')
        rby=input('Which door do you choose: Red, Blue or Yellow?\n').upper().strip()[0]
        if rby=='Y':
            print('Wow!!!You find a big treasure: $100000 dollars, go waste it...')
        else:
            print('Well, you almost make it, but choose the wrong door...Hehehe, attacked by a monstruous Bear!!!')
    else:
        print('hehehe, you were attacked by sharks...')
else:
    print('Hehehe, You fall into a cave with snakes...')