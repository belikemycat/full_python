import random
import time


def spin_row():
    symbols = ['🍒', '🍉', '🪙', '🍋', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" ".join(row))
def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🪙':
            return bet * 5
        elif row[0] == '🍋':
            return bet * 7
        elif row[0] == '⭐':
            return bet * 10
    return 0
def main():
    balance = 500
    print("****************************")
    print("Welcome to Slot machine game!")
    print("Symbols :🍒 🍉 🪙 🍋 ⭐")
    print("****************************")

    while balance>0:
        print(f'Current balance is:{balance:.2f}$')

        bet = (input(f"Enter the bet:"))

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet>balance:
            print("Insufficient funds.")
            continue
        if bet<=0:
            print("Invalid choice.")
        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        #time.sleep(1)
        print_row(row)

        payout = get_payout(row,bet)

        if payout>0:
            print(f'You won {payout:.2f}$')
        else:
            print('Sorry , you lost this round :(')

        balance += payout

        play_again = input("Do you want to play again Y/N: ")
        if play_again.upper() != 'Y':
            break

    print(f"Game over!Your final balance is {balance}")

if __name__ == "__main__":
    main()

