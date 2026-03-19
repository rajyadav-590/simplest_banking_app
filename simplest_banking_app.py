def balance_():
    print(f"Your balance is: ₹{balance}")
    print("===========================")


def deposit(deposit_money):
    global balance
    if deposit_money <= 0:
        print("Invalid amount! Try again...")
    else:
        balance += deposit_money
        print("Money deposited successfully..")
        print(f"Updated balance: ₹{balance}")
        print("===========================")


def withdraw(withdrawn_money):
    global balance
    if withdrawn_money <= 0:
        print("Invalid amount!")
    elif withdrawn_money > balance:
        print("Insufficient balance..")
    else:
        balance -= withdrawn_money
        print("Money withdrawn successfully..")
        print(f"Updated balance: ₹{balance}")
        print("===========================")


balance = 0.0

if __name__ == "__main__":
    print("Welcome to ABC Bank")

    while True:
        print("\nChoose one option:")
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("6. Quit")
        print("===========================")

        user_input = input("Enter your choice: ")

        if user_input == "1":
            balance_()

        elif user_input == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                deposit(amount)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif user_input == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif user_input == "6":
            print("Thanks for banking with us.")
            break

        else:
            print("Invalid input! Try again.")

        # 👉 Continue or exit option
        choice = input("Do you want to continue? (yes/no): ").lower().strip()
        if choice != "yes":
            print("Thanks for banking with us.")
            break
