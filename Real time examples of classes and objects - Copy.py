class bankacc():
    def __init__(self,name,accno):
        self.n=name
        self.a=accno
        self.balance=0
def deposit(self,amount):
        self.balance = self.balance + amount
        print("you account balance is ",self.balance)

def withdraw(self,amount):
        self.balance= self.balance - amount
        print("you account balance is ",self.balance)


deepika=bankacc("deepika","1234")
titi=bankacc("guvi","1111")

print(deepika)
print(titi)
