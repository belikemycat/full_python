"""python banking program
functions,nested loops
Just a banking program to check balance,deposit,withdraw operations  , mainly written for revision"""
def show_balance(balance):
    print(f'Your balance is ${balance:.2f}')
def deposit(balance):
    amount = float(input("Enter the amount of money to be deposited: "))
    if amount < 0:
        print("That is not a valid amount ")
        return 0
    else:
        return amount
def withdraw(balance):
    Wamount = float(input("Enter the amount of money to be withdrawn: "))
    if Wamount > balance:
        print("Insufficient funds")
        return 0
    if Wamount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return Wamount
def main():
    print("********************")
    balance = 0
    isactive = True
    while isactive:
        print("Hello!")
        print("1.Show the balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("********************")
        choice = input("Enter your choice, please(1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance =+ deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            isactive = False
        else:
            print("Invalid choice")
    print("Thank you!")
if __name__ == "__main__":
    main()