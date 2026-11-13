# create a bank account eith members account number ,name,type of account and balance.
# write constructor and methods to deposit at the bank and withdraw an amount from the bank
class bank:
    def __init__(self):
        self.balance=0
    def deposit(self):
        amount=float(input("enter amount to be deposited : "))
        self.balance = self.balance+amount
        print("\n amount Deposited : ",amount)
    def withdraw(self):
                  amount=float(input("enter amount to be withdrawn: "))
                  if self.balance>=amount:
                     self.balance=self.balance-amount
                     print("\n amount withdrwan successfully : ",amount)
                  else :
                    print("\n insufficient balance")
    def display(self):
                             print("\n available balance",self.balance)
bobj = bank()

while True:
    print("\n1: Deposit Money")
    print("2: Withdraw Money")
    print("3: Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        bobj.deposit()
        bobj.display()

    elif ch == 2:
        bobj.withdraw()
        bobj.display()

    elif ch == 3:
        break

    else:
        print("Invalid choice!")

bobj.display()