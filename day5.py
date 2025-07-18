
          
#--------------------------------------------------
import random
print("Welcome to password generator by python")  
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                     'u', 'v', 'w', 'x', 'y', 'z']  
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
           '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"',
           ',', '<', '.', '>', '/', '?', '`', '~']  

# nr_charachter=int(input(f"how many charachter would you like in your password? please choose a number between 8 and 16\n"))
# nr_letter=int(input(f"how many letters would you like in your password?\n"))
# nr_number=int(input(f"how many numbers would you like in your password?\n"))
# nr_symbol=int(input(f"how many symbols would you like in your password?\n"))
# password=''
# for n in range(1,nr_letter+1):
#  password+=random.choice(letters)
# for n in range (1, nr_number+1):
#  password+=random.choice(digits)
# for n in range(1, nr_symbol+1):
#  password+=random.choice(symbols)
# print(password) 

#----------------------------------------------------------------------------------------
nr_charachter=int(input(f"how many charachter would you like in your password? please choose a number between 8 and 16\n"))
nr_letter=int(input(f"how many letters would you like in your password?\n"))
nr_number=int(input(f"how many numbers would you like in your password?\n"))
nr_symbol=int(input(f"how many symbols would you like in your password?\n"))
password=[]
for n in range(1,nr_letter+1):
 password.append(random.choice(letters))
for n in range (1, nr_number+1):
 password.append(random.choice(digits))
for n in range(1, nr_symbol+1):
 password.append(random.choice(symbols))
random.shuffle(password) 
#turn list to string
passwordlist=""
for char in password:
 passwordlist+=char

#or ''.join(['a', 'b', 'c'])  →  'abc'
#password_str = ''.join(password)
 
print(f"your password is: {passwordlist}")  