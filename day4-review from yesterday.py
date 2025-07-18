import random
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")    
# -----------------------
# building map :x3
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

map = [row1, row2, row3]

# the golden  hidden box
treasure_row = 1
treasure_col = 1

# user guess
while True:
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Enter position (e.g. 23 means column 2 and row 3): ")
    if len(position) !=2 or not position.isdigit():
        print(" ‼️ invalid input, please enter a 2-digit number  like 21")
        continue
    col = int(position[0])
    row = int(position[1])
    if col < 1 or col > 3 or row < 1 or row > 3:
        print("❗ Position out of range. Use numbers from 1 to 3.")
        continue

    # check if the user would find the golden box
    if row == treasure_row and col == treasure_col:
        map[row - 1][col - 1] = "🏆"
        print("🎉 You found the treasure!")
        print(f"{row1}\n{row2}\n{row3}")
        break
    else:
        if map[row - 1][col - 1] == "❌":
            print("🔁 You already guessed that spot.")
        else:
            map[row - 1][col - 1] = "❌"
            print("❌ No treasure here. Try again.")

    
    

