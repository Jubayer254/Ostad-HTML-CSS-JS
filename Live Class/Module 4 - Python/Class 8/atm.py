def atm():
    print("Welcome to ATM")
    pin = '1234'
    balance = 1000

    while True:
        Ppin = input("Enter Your PIN: XXXX (or type 'exit' to quit): ")
        if Ppin == pin:
            print("\n1. Check Balance\n2. Withdraw Money\n3. Deposit Money\n4. Change PIN\n5. Exit")
            choice = input("Enter a Number: ")
            if choice == '1':
                print("Your Balance is: ",balance)
            elif choice == '2':
                amount = float(input("\nEnter the Amount to Withdraw: "))
                if balance < amount:
                    print("Insufficient Balance")
                else:
                    balance -= amount
                    print(f"{amount} has been withdrawn\nRemaining Balance: {balance}")
            elif choice == '3':
                amount = float(input("\nEnter the Amount to Diposit: "))
                balance += amount
                print(f"{amount} has been withdrawn\nUpdated Balance: {balance}")
            elif choice == '4':
                new_pin = input("\nEnter 4 digit PIN: ")
                if len(new_pin) != 4 or not (new_pin.isdigit()):
                    print("Invalid PIN")
                else:
                    pin = new_pin
                    print("\nPIN Changed Successfully")
            elif choice == '5':
                print("\nThank you for using the ATM! Goodbye.")
                break
        elif Ppin.lower() == 'exit':
            print("\nThank you for using the ATM! Goodbye.")
            break
        else:
            print("\nIncorrect PIN, please try again\n")

atm()