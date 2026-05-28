class BankAccount:
    def __init__(self, account_number, username, pin) :
        self.account_number = account_number
        self.username = username
        self._balance = 0
        self._pin = pin
        self.transactions = []
        self.transactions.append("Account Created")
    
    def deposit(self, amount):
        if(amount > 0):
            self._balance += amount
            print(f"Deposited ${amount}")
            self.add_transaction(f"Deposited ${amount}")
        else: 
            print("Invalid deposit amount") 

    def withdraw(self, amount, pin):
        if not self.verify_pin(pin):
            print("Incorrect PIN")
            return False
        if amount <=0:
            print("Invalid withdrawal amount")
            return False
        if self._balance < amount:
            print("Insufficient Balance")
            return False
        self._balance -=amount
        print(f"Withdrawn ${amount}")
        self.add_transaction(f"Withdrawn ${amount}")
        return True
            
    def check_balance(self, pin):
        if self.verify_pin(pin):
            print(f"Current Balance is ${self._balance}")
        else: 
            print("Incorrect PIN")

    def show_transaction(self, pin):
        if(self.verify_pin(pin)):
            if not self.transactions:
                print("No transaction found")
                return
            for transaction in self.transactions:
                print(transaction)
        else: 
            print("Incorrect PIN")

    def add_transaction(self, message):
        self.transactions.append(message)
            
    def verify_pin(self, pin):
        return pin == self._pin
        
    def change_pin(self,old_pin, new_pin):
        if(self.verify_pin(old_pin)):
            self._pin = new_pin
            print("PIN changed successfully")
            self.add_transaction("PIN changed")
        else: 
            print("Wrong PIN entered")
            
    def account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.username}")
        # print(f"Account Balance: {self._balance}")
        
    
if __name__ == "__main__":
    pass