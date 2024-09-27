import random
#dice roller program
#●┌ ─ ┐ │ └ ┘ - the used symbols to draw the dice xD
#print("\u25CF\u250C \u2500 \u2510 \u2502 \u2514 \u2518") thats how we get some symbols
diceQ = {
    1: ("┌───────────┐",
        "│           │",
        "│     ●     │",
        "│           │",
        "└───────────┘"),
    2: ("┌───────────┐",
        "│  ●        │",
        "│           │",
        "│        ●  │",
        "└───────────┘"),
    3: ("┌───────────┐",
        "│  ●        │",
        "│     ●     │",
        "│        ●  │",
        "└───────────┘"),
    4: ("┌───────────┐",
        "│  ●     ●  │",
        "│           │",
        "│  ●     ●  │",
        "└───────────┘"),
    5: ("┌───────────┐",
        "│  ●     ●  │",
        "│     ●     │",
        "│  ●     ●  │",
        "└───────────┘"),
    6: ("┌───────────┐",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "└───────────┘"),
}
dice = []
total = 0

quantity_dice = int(input("How many dices: "))

for die in range(quantity_dice):
    dice.append(random.randint(1,6))

for die in range(quantity_dice):
    for line in diceQ.get(dice[die]):
        print(line)

for die in dice:
    total += die
print(f'Total is {total}')