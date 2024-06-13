#Hangman Game

import random
import HangmanWords
random_word=random.choice(HangmanWords.word_list)



lr_word=[]
for _ in range(len(random_word)):
    letter_1=random_word[_]
    lr_word+=letter_1
# lr_w=lr_word.remove(' ')
# print(lr_word)
print("Welcome to Hangman's Python\nYou have 6 lives\nThe word you need to guess has {} letters. Good Luck!".format(len(random_word)))

blank=[]
for pos in range(len(random_word)):
    add_blank=blank.append('_')
#   blank+="_"

lives=6
game_over=True
while game_over:
    user_guess=input('Choose a letter:\n').lower()
    for position in range(len(random_word)):
        letter=random_word[position]
        if letter == user_guess:
            blank[position]=user_guess
    print(blank)
    if user_guess not in lr_word:
        lives-=1
    if lives==0:
        game_over=False
        print("Well, you lost!")
        print('The word was {}'.format(random_word))
    elif blank==lr_word:
        game_over=False
        print('Wow!!!You Won!!!')