from bank import Bank
bank = Bank()
while True:
    print("\n =========== BANK MENU ===========")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. Show All Accounts")
    print("7. Delete Account")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if(choice == "1"):
        account_number = int(input("Enter Account Number: "))
        username = input("Enter Holder name: ")
        pin = input("Set PIN: ")
        bank.create_account(account_number, username, pin)
    elif choice == "2":
        account_number = int(input("Enter account number: "))
        try :
            amount = float(input("Enter Amount: "))
        except ValueError:
            print("Invalid amount")
        # pin = input("Enter PIN: ")
        bank.deposit_to_account(account_number, amount)
    elif choice == "3":
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter Amount: "))
        pin = input("Enter PIN: ")
        bank.withdraw_from_account(account_number, amount, pin)
    elif choice =="4":
        account_number = int(input("Enter account number: "))
        pin = input("Enter PIN: ")
        bank.check_balance(account_number, pin)
        
    elif choice =="5":
        sender_account = int(input("Enter Sender Account Number: "))
        receiver_account = int(input("Enter Receiver Account Number: "))
        amount = float(input("Enter Amount: "))
        pin = input("Enter PIN: ")
        bank.transfer_money(sender_account, receiver_account, amount, pin)
    elif choice == "6":
        bank.show_all_accounts()
    elif choice == "7":
        account_number = int(input("Enter account number: "))
        pin = input("Enter PIN: ")
        bank.delete_account(account_number, pin)
    elif choice == "8":
        print("Thank you for using the bank system")
        break
    else: 
        print("Invalid Choice")
        
