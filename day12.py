# enemies=1
# def increase_enemi():
#     enemies=2
#     print(f"the number of enemies_1 is:{enemies}")
# increase_enemi()
# print(f"the number of enemies_2 is:{enemies}")
import random
secret_number=random.randint(0,100)

game_hardness=input("do you want a hard game please type 'hard', or you want a easy one type'easy' : ").lower()

def guess_left(game_hardness):
    if game_hardness=="easy":
       return 10
    
    elif game_hardness=="hard" :
      return  5 
    else:
        print("invalid input, defaulting to hard mode") 
        return 5 
guess_attempt=guess_left(game_hardness)
while guess_attempt>0:
    try:
        your_guess= int(input("please enter a random number between 1 and 100:\n "))
    except ValueError :
        print("Invalid number.  your number must be between 1 and 100") 
        continue  
    if your_guess<1 or your_guess>100:
        print("Your number must be between 1 and 100.")
        continue

    if your_guess> secret_number:
        guess_attempt-=1
    
        print(f"too high,just {guess_attempt} guess left" ) 
    elif your_guess<secret_number:
        guess_attempt-=1
        print(f"too low,just {guess_attempt} guess left" )
    else:
        print("you win")
        break
if guess_attempt==0:
    print(f"you have run out of attempt, you lose .the secret number was : {secret_number} ")


# -------------------------------------------
# from random import randint
# from art import logo

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()
