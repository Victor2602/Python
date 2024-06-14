alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
    end_text=""
    if direction=="D":
        shift*=-1    
    for i in text:
        if i not in alphabet:
            end_text+= i
        else:
            position_letter=alphabet.index(i)
            cryption_letter=position_letter+shift
            end_text+=alphabet[cryption_letter%26]   
    if direction=="D":
        print("Here's the decoded result: {}".format(end_text))
    else:
        print("Here's the encoded result: {}".format(end_text))


direction_1=True

while direction_1==True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").upper()[0]
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))
    shift= shift%26
    caesar(text,shift,direction)
    play_again=input("Type 'yes' if you want to go again. Otherwise tipe 'no'.\n").upper().strip()[0]
    if play_again=="Y":
        direction_1=True
    else:
        print('Goodbye.')
        direction_1=False
