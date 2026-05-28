from account import BankAccount

class Bank:
    def __init__(self):        
        self.accounts = {}

    def create_account(self, account_number, username, pin):
        if account_number in self.accounts:
            print("Account already exists")
            return
        new_account = BankAccount(account_number, username, pin)
        self.accounts[account_number] = new_account
        print("Account created successfully")
        
    def find_account(self, account_number):
        return self.accounts.get(account_number) #safer than self.account[account_number] 
    
    def deposit_to_account(self, account_number, amount):
        account = self.find_account(account_number)
        if not account:
            print("Account not found")
            return
        account.deposit(amount)

    def withdraw_from_account(self, account_number, amount, pin):
        account = self.find_account(account_number)
        if not account:
            print("Account not found")
            return
        account.withdraw(amount,pin)

    def check_balance(self,account_number, pin):
        account = self.find_account(account_number)
        if not account:
            print("Account not found")
            return
        account.check_balance(pin)
    def transfer_money(self, sender_acc, receiver_acc, amount, pin):
        sender = self.find_account(sender_acc)
        receiver = self.find_account(receiver_acc)
        if not sender:
            print("Sender account not found")
            return
        if not receiver: 
            print("Receiver account not found")
            return
        
        success = sender.withdraw(amount, pin)
        if not success:
            # print("Transaction Failed due to insufficient balance or incorrect pin")
            return 
        # sender._balance -= amount 
        receiver._balance += amount

        sender.transactions.append(f"Transferred ${amount} to {receiver_acc}")
        receiver.transactions.append(f"Received ${amount} from {sender_acc}")
        print("Transfer Successful")

    def show_all_accounts(self):
        # account = self.find_account(account_number)
        if not self.accounts:
            print("No accounts available")
            return
        for account in self.accounts.values():
            print("Account Number:", account.account_number)
            print("Holder Name:", account.username)
            print("--" * 30)
            
    def delete_account(self, account_number, pin):
        account = self.find_account(account_number)
        if not account:
            print("Account not found")
            return
        if account.pin != pin:
            print("Incorrect PIN")
            return
        del self.accounts[account_number]
        print("Account deleted successfully")


