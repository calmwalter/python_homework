class Account:
    def __init__(self,id=0,balance=100,annualInterestRate=0):
        self.__id=id
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate
    def getId(self):
        return self.__id
    def getBalance(self):
        return self.__balance
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    def setId(self,id):
        self.__id=id
    def setBalance(self,balance):
        self.__balance=balance
    def setAnnualInterestRate(self,annualInterestRate):
        self.__annualInterestRate=annualInterestRate
    def getMonthlyInterestRate(self):
        return self.getAnnualInterestRate()/12 
    def getMonthlyInterest(self):
        return self.getBalance()*self.getMonthlyInterestRate()/100
    def withdraw(self,amount):
        self.setBalance(self.getBalance()-amount)
    def deposit(self,amount):
        self.setBalance(self.getBalance()+amount)

ac=[Account() for i in range(10)]
while True:
    id=eval(input("Enter an account id:"))
    if id<0 or id >9:
        print("Please enter an correct id.")
        continue
    print("Main menu\n1: check balance\n2: withdraw\n3: deposit\n4: exit")
    
    while True:
        x=eval(input())
        if x==1:
            print("Current balance:",ac[id].getBalance())
        elif x==2:
            ac[id].withdraw(eval(input("How much money for withdraw:")))
        elif x==3:
            ac[id].deposit(eval(input("How much money for deposit:")))
        elif x==4:
            break
        print("Main menu\n1: check balance\n2: withdraw\n3: deposit\n4: exit")