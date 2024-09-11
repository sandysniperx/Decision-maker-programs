import random

per_1 = input("Player1: ")
per_2 = input("Player2: ")
print(f"Player1 ({per_1}) always goes first.")

while True:
    roll_c = input("Roll the dice? (y/n):")       
    if roll_c == "n":
        print("Whats the point of me then?")
    else:
        dice = list(range(1,7))
        dice_roll = random.choice(dice)
                    
        print(f"{per_1} rolled a {dice_roll}.")
