class bank:
    def __init__(self,account_number,balance = 0):
        self.account_number = account_number
        self.balance = balance 

    def deposit(self,amount):
        if amount > 0 :
            print(f"rupees {amount} has been credited to your account")
        else:
            print("error: invalid amount")
    
    def withdraw(self,amount,balance):
        if amount > 0 and amount<balance:
            print(f"rupees {amount} has been withdrawn from your account")
        else:
            print("low balance")
    
    def check_balance(self,balance):
        print(f"current {balance} rupees")

bank.deposit(0,1000)
bank.check_balance(0.1000)
