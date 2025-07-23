



import random
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
from art import logo_3
print("welcome to blackjack program")
def calculate_scores(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    
    return card
def compare_score(user_scores, computer_scores):
    if user_scores==computer_scores:
        print(" its draw!")
    elif computer_scores ==0 :
        print("oponent lose , you win!😎")
    elif user_scores==0:
        print("you lose 😒")
    elif user_scores>21:
        print("you went over, you lose") 
    elif computer_scores>21:
        print("you win, your opponent lose lose") 

    elif user_scores>computer_scores:
        print("you win, congratulation babe 🎉🎉🎉")
    else:
        print("your opponent win. sorry")    
def play_game():
    print(logo_3)    
    user_card=[]
    computer_card=[]
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
        
    game_over=False
    while not game_over:
        user_scores=calculate_scores(user_card)
        computer_scores=calculate_scores(computer_card)
        print(f"your card is:{user_card} and current score is{user_scores}")
        print(f"computer first card is:{computer_card[0]}")
        if computer_scores==0 or user_scores==0 or user_scores>21:
            game_over=True
        else:
            user_should_continue=input("if user want to continue  type 'y' otherwise type 'n'  ")
            if user_should_continue=='y':
                user_card.append(deal_card())
            else:
                game_over=True
    while computer_scores !=0 and computer_scores<17:
        computer_card.append(deal_card())
        computer_scores=calculate_scores(computer_card)
    print(f"Your final hand: {user_card}, final score: {user_scores}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_scores}")    
    print(compare_score(user_scores, computer_scores))
while input("do you want to play a new game say 'y' and dont you want say 'n' ....")== 'y':
    clear()
    play_game()




# # ♠️ Blackjack — Game Overview
# Blackjack (also called 21) is a popular card game played at casinos. It’s usually played between players and the dealer (not between players themselves).

# 🎯 Goal of the game:
# Get a hand total as close to 21 as possible without going over.

# 🃏 Card Values:
# Cards 2 through 10 = face value

# J (Jack), Q (Queen), K (King) = 10 points

# A (Ace) = 1 or 11 points (whichever helps your hand more)

# Example hands:
# A + 10 = 21 → this is a Blackjack

# 9 + 7 = 16

# K + 6 = 16

# A + 5 + 3 = either 9 or 19 (Ace can be 1 or 11)

# 🧑‍🤝‍🧑 Who plays?
# One dealer

# 1 or more players

# Players play against the dealer, not against each other.

# 🔁 How the game works (step-by-step):
# 1. Start of the game
# Each player and the dealer get two cards.

# Players' cards are face up.

# Dealer has one card face up and one face down (called the "hole card").

# 2. Player's Turn
# Each player decides what to do:

# Option	Meaning
# Hit	Ask for another card
# Stand	Keep your current hand
# Double Down	Double your bet, take 1 more card, then stand
# Split	If you have two same cards (e.g. 8-8), split into two hands

# Player can hit multiple times, but if total goes over 21, they bust (lose automatically).

# 3. Dealer's Turn
# After all players finish:

# Dealer reveals their hidden card.

# Dealer must hit until their total is 17 or more.

# If dealer busts (>21), all remaining players win.

# 🏆 Winning the game
# You win if:

# Your total is closer to 21 than the dealer, or

# Dealer busts, and you didn't

# You lose if:

# You bust, or

# Dealer has a higher total (≤ 21)

# 💵 Special case: Blackjack
# If your first two cards are A + 10 (or face card) → this is called Blackjack.

# It beats any other hand, even if the total is 21 in more than 2 cards.

# Blackjack usually pays 3:2 (e.g. you bet $10, you win $15)

# 🛑 Summary of Key Rules:
# Try to reach 21 without going over

# Face cards = 10, Ace = 1 or 11

# Beat the dealer’s hand or wait for them to bust

# Blackjack (Ace + 10) is the best possible hand    
    
  
    مراحل کلی اجرای بازی بلک‌جک (Blackjack) که در کدی که نوشتی پیاده‌سازی شده، به‌صورت زیر هست:

🟢 مرحله 1: آماده‌سازی
import random, os, و logo_3 برای آماده‌سازی برنامه.

تابع clear() برای پاک کردن صفحه‌ی کنسول.

تعریف لیست کارت‌ها (2 تا 11 و کارت‌های تصویری به‌صورت 10).

🟢 مرحله 2: تعریف توابع
deal_card():
یک کارت تصادفی از لیست کارت‌ها انتخاب می‌کند.

calculate_scores(cards):

اگر جمع کارت‌ها برابر ۲۱ و فقط دو کارت داشتیم، بازیکن "بلک‌جک" کرده و نمره‌اش 0 می‌شود.

اگر کارت 11 (آس) داریم و جمع کارت‌ها بیشتر از 21 است، آس را به 1 تبدیل می‌کنیم.

در نهایت جمع کارت‌ها برمی‌گردد.

compare_score(user_scores, computer_scores):
منطق برنده یا بازنده بودن را مشخص می‌کند.

🟢 مرحله 3: اجرای بازی با play_game()
چاپ لوگوی بلک‌جک.

دو کارت اولیه برای بازیکن و کامپیوتر داده می‌شود.

بررسی می‌شود:

آیا کسی بلک‌جک دارد؟

آیا کارتی بیش از 21 شده؟

بازیکن می‌تواند کارت بکشد (y) یا بازی را متوقف کند (n).

پس از توقف بازیکن، کامپیوتر کارت می‌کشد تا نمره‌اش به حداقل 17 برسد.

🟢 مرحله 4: اعلام نتیجه
کارت‌ها و امتیاز نهایی بازیکن و کامپیوتر چاپ می‌شود.

با compare_score() برنده مشخص می‌شود.

🟢 مرحله 5: شروع بازی جدید
با دستور:

python
Copy
Edit
while input("do you want to play a new game say 'yes' ...") == 'y':
تا وقتی کاربر بخواد، بازی جدید شروع میشه و صفحه پاک میشه (clear()).
