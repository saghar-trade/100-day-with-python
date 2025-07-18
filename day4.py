
#----------------------------------------------
import random

Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images=[Rock, Paper, Scissors]
user_choice =  int(input("what do you choose? type 0 for Rock , 1 for Paper and 2 for scissor. "))
if user_choice>=3 or user_choice<0: 
 print(" you entered an invalid number!!, you lose.") 
else:
 print(game_images[user_choice])
 computer_choice= random.randint(0, 2)
 print(f" computer chose {computer_choice}")
 print(game_images[computer_choice])
  
 if (user_choice == 0 and computer_choice == 2 ):
  print("you wins")
 elif (user_choice == 2 and computer_choice == 0 ):
  print("you lose")
 elif computer_choice > user_choice:
  print("you lose!")
 elif user_choice > computer_choice:
  print("you win!")
 elif user_choice == computer_choice:
  print(" it's a draw")