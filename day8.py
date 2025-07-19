

#--------------------------------


from art import logo
print(logo)
Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                     'u', 'v', 'w', 'x', 'y', 'z' ] 
# or ALPHABET = list(string.ascii_lowercase) 
def caesar (start_text, shifted_number, cipher_direction):
        end_text=""
        for letter in start_text:
            if letter in Alphabet:
                position=Alphabet.index(letter)
                if cipher_direction== "encode":
                    new_position=position +  shifted_number
                elif cipher_direction=="decode":
                    new_position=position -  shifted_number
                end_text +=Alphabet[new_position]
            else:
                end_text+= letter
        print(f"your plain text is: {end_text}")
should_continue=True
while should_continue:
    direction=input("type 'encode' for encrypt or type 'decode' for decrypt\n")
    text=input( " please enter your message\n").lower()
    shift=int(input("please input the shift number\n"))
    shift=shift % 26
    caesar(start_text=text , shifted_number=shift ,cipher_direction=direction )
    result= input("type 'yes' if you want to continue, and type'no' if yoy dont: ")
    if result=="no":
        should_continue=False
   

    
    
   
print("Good bye Dear!")