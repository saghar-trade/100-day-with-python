

Stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']



import random
import hangman
chosen_word=random.choice(hangman.word_list)
display=[]
lives=6 
for _ in chosen_word:
    display.append("_")
while "_" in display and lives>0:
    guess=input('Guess a letter:').lower()
    found=False   
    for n in range(0,len(chosen_word)):
            if chosen_word[n]==guess:
                display[n]=guess
                found = True
    if found:
        print("Right")
    else:
        lives-=1
        Current_stage=Stages[lives] 
        print(" your guess is Wrong")
        print(f" your hanging man status is:{Current_stage}")
    print(" ".join(display))
if "_" not in display:
    print("You guessed the word! 🎉")
else:
     print(f"You lost! The word was: {chosen_word}")