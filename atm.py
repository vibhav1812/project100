from asyncore import read


class Atm(object):
    def __init__(self, cardNo, pinCode, amount):
        self.cardNo = cardNo
        self.pinCode = pinCode
        self.amount = amount

    def cardLogin(self):
        cardEntry = int(input("To withdraw/deposit/check cash please enter your card number: "))
        pinEntry = int(input("Input your pin: "))
       
        if cardEntry == self.cardNo:
            if pinEntry == self.pinCode:
                print("Login Successful")
            else:
                print("Your pin is incorrect")
        else:
            print("Card Number does not exist")

    def withdrawCash(self):
        amountEntry = int(input("Enter the amount you want to withdraw: "))
        if amountEntry <= self.amount:
            self.amount = self.amount - amountEntry
            print(f"Withdrawl successful! Your current balance is {self.amount}")
        else:
            print(f"You don't have {amountEntry}, your current balance is {self.amount} only")

    def depositCash(self):
        depositEntry = int(input("Enter the amount you want to deposit: "))
        self.amount = self.amount + depositEntry
        print(f"Your current amount is: {self.amount}")

    def checkBalance(self):
        print(f"This is your current balance: {self.amount}")

    def main(self):
        print("Welcome!")
        self.cardLogin()
        userActivity = True

        while userActivity == True:
            message = input("Enter 'w' to withdraw, 'd' to deposit, 'b' to check balance or c to exit: ")
            if message == 'w':
                self.withdrawCash()
            elif message == 'd':
                self.depositCash()
            elif message == 'b':
                self.checkBalance()
            elif message == 'c':
                print("Thank You")
                userActivity == False
                break

card1 = Atm(123,456,1000)
card1.main()