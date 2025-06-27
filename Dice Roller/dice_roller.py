import random

# dice ASCII art for values 1 - 6
DICE_ART = {
    1: (
        "┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘",
    ),
    2: (
        "┌─────┐",
        "│ ●   │",
        "│     │",
        "│   ● │",
        "└─────┘",
    ),
    3: (
        "┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘",
    ),
    4: (
        "┌─────┐",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘",
    ),
    5: (
        "┌─────┐",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘",
    ),
    6: (
        "┌─────┐",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘",
    ),
}
def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]
    
def display_dice(dice_values):
    rows = [""] * 5 # each die is 5 rows
    for value in dice_values:
        art = DICE_ART[value]
        for i in range(5):
            rows[i] += art[i] + "  " # add spacing between dice
        for row in rows:
            print(row)
            
def main():
    print("🎲 Dice Roller 🎲")
    while True:
        try:
            num = int(input("How many dice do you want to roll? (1-6): "))
            if 1 <= num <= 6:
                break
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Thats not a valid number.")
    rolled = roll_dice(num)
    display_dice(rolled)
    
    again = input("Roll again? (y/n): ").lower()
    if again == 'y':
        print()
        main()
    else:
        print("Goodbye!")
        
if __name__ == "__main__":
    main()