import random
#d=["00","11","22"]
w=["01","12","20"]
l=["02","10","21"]

answer=False
while not answer==True:
    rsp_game=int(input('What do you choose?\n0 for rock, 1 for scissors, 2 for paper...\n'))
    dwl=['Rock','Scissors','Paper']
    rsp_CPU=random.randint(0,2)
    while rsp_game==rsp_CPU:
        print('Wow!!!It is a draw...')
        rsp_game=int(input('What do you choose?\n0 for rock, 1 for scissors, 2 for paper...\n'))
    p=f"{rsp_game}{rsp_CPU}"
    if p=="01" or p=="12" or p=="20":
        rsp_game=dwl[rsp_game]
        rsp_CPU=dwl[rsp_CPU]
        print("Well played!!! You won!!!You played {} and the computer played {}.".format(rsp_game,rsp_CPU))
    else:
        rsp_game=dwl[rsp_game]
        rsp_CPU=dwl[rsp_CPU]
        print("Hehehe...The computer won!!!It played {},whilst you played {}.".format(rsp_CPU,rsp_game))
    answer_1=input('Do you want to play again? Yes or No\n').upper().strip()[0]
    if answer_1=='N':
        answer=True
#rsp=['1','2']



