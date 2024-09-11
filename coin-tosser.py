import random

per_1 = input("person1: ")
per_2 = input("person2: ")

while True:
    actions = ["heads","tails"]
    picker = input(f"{per_1} chooses (heads/tails): ")

    toss = random.choice(actions)

    print(f"Its {toss}.")
    
    if picker == toss:
        print(f"{per_1} wins, better luck next time {per_2}.")
    else:
        print(f"{per_2} wins, better luck next time {per_1}.")
    
    user_retry = input("go again? (y/n):")
    if user_retry == "y":
        print("recalibrating coins...")
    else:
        print("gg")
        break