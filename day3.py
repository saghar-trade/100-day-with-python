print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print("Welcome to Treasure Island")
print("Your Mission Is to Find Treasure")
choice1 = input('You are at the crossroad, which path do you want to go? Type  "lefrt" or "right" .\n' ).lower()
if choice1 == "left":
   choice2 = input("you've come to a lake, there is an island in the middle of lake. do you want to 'wait' for a bout or do you want to 'swim' until the island. plase type 'wait' or 'swim'\n ").lower()
   if choice2=="wait":
       choice3=input('you are arrived at island unharmed. there is a house with three doors. one "blue", one "red" and one "yellow", which color do you choose?\n' ).lower()
       if choice3== "red":
           print("the room  is full of fire. Game over.")
       elif choice3== "yellow":
           print("you found the treasure. You Win.")
       elif choice3== "blue":  
           print("you enter the room full of beasts. Game Over.")   
       else:
           print("you chose the door that does not exist. Game Over.")       
   else:
       print("you are attacked by an angry trout. Game over. ")    
else:   
    print('You fell in a holl, GAME OVER .')
