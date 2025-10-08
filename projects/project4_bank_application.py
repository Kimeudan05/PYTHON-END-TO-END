from datetime import datetime,timezone
# deposit and withdraw cash
class BankAccount:
    def __init__(self,owner,balance=0):
        #private attributes
        self._owner = owner 
        self._balance = balance
        self._transactions =[] # a list to hold transactions
        
        # record account creation
        self.__add_transactions("Account opened",0)
        
    # string representation
    def __str__(self):
        return f"{self._owner}'s balance is {self._balance:,.2f}"
    
    # getters
    def get_owner(self):
        return self._owner
    
    def get_balance(self):
        return self._balance
    
    #private method to log transactions
    def __add_transactions(self,transaction_type,amount):
        time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        self._transactions.append({
            "type":transaction_type,
            "amount":amount,
            "balance":self._balance,
            "time":time
        })
    
    # setter for setting balance directly (for demo)
    def set_balance(self,new_balance):
        if new_balance >=0:
            self._balance = new_balance
        else:
            print("Balance cannot be negative")
    
    # Methods
    # deposit method
    def deposit(self,amount):
        if amount >0:
            self._balance += amount
            self.__add_transactions("Deposit",+amount)
            print(f"{amount:,.2} deposited successifuly")
        else:
            print("Amount must be greater than zero !")
            
    # Withdraw method
    def withdraw(self,amount):
        if amount > self._balance:
            print(f"Insufficient funds ! your balance is {self._balance:,.2f}")
            
        elif amount <=0:
            print("Amount must be greater than zero !")     
        else:
            self._balance -= amount
            self.__add_transactions("Withdrawal",-amount) # Negative for clarity
            print(f"{amount:.2f} withdrawn successifully")
           
    # show all transactions
    def show_transactions(self):
        if not self._transactions:
            print("No transactions found")
            return
        
        print("\n Transaction History:")
        print("-"*50)
        for txn in self._transactions:
            print(f"{txn['time']} | {txn['type']:<12} | Amount: {txn['amount']:>10,.2f} | Balance :{txn['balance']:>10,.2f}")
        print("-"*50)

# Main program
def main():
    print("Welcome to ChatBank")
    account = BankAccount("Masila",1000)
    
    while True:
        try:
            choice = int(input("\n1: Show Balance\n2: Deposit\n3: Withdraw\n4: Set Balance (demo setter)\n5 : Transaction History\n6: Exit\nChoice: "))        
        except ValueError:
            print("Please enter a valid number :")
            continue
        if choice ==1:
            print(account)
        elif choice == 2:
            try:
                amount = float(input("Enter the amount you wish to deposit :"))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount!")
                
        elif choice ==3:
            try:
                amount = float(input("Enter the amount you wish to withdraw :"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount!")
                
        elif choice == 4:
            # setter demo for a demo balance
            try:
                new_balance = float(input("Set new balance (for demo) :"))
                account.set_balance(new_balance)
            except ValueError:
                print("Invalid number")
                
        elif choice == 5:
            account.show_transactions()
            
        elif choice ==6:
            print(f"Goodbye, {account.get_owner()}! You exited with a balance of {account.get_balance():,.2f}")
            break
        else:
            print("Invalid option try again")
main()

# next improvements
# 1 .Add user login/password protection
# 2. Handle multiple accounts