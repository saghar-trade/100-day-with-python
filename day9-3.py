import os
def clear():
    os.system("cls" if os.name=="nt" else "clear")
bids={}
def blind_auction(bider_person,bider_price):
    bids[bider_person]=bider_price 
    print(bids)  

def find_highest_bider():
    highest_price=0
    winner=''
    for bidder in bids:
        if bids[bidder]>highest_price:
            highest_price=bids[bidder]
            winner=bidder
    return winner,highest_price        
     

is_bid=True
while is_bid:
    name= input("type your name :")
    price=int(input("type your price: $"))
    blind_auction(name, price)
    result=input("type 'yes' if there is any other person, and type'no' if there is not: ").lower()
    if result=="no":
        is_bid=False
    else:
        clear()
winner, highest_price = find_highest_bider()
for person , price in bids.items():
    print(f"{person}:{price}") 
print(f"The winner is {winner} with a bid of ${highest_price}.")        
