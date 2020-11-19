class Atm(object):
    def __init__(self, number, pin):
        self.number = number
        self.pin = pin
        self.balance = 100

    def withdrawl(self, amt):
        self.balance -= amt

    def deposit(self, amt):
        self.balance += amt

print("  ===============  ATM  ===============  \n")

number = int(input("Enter Card Number: "))
pin = int(input("Enter Pin: "))

atm = Atm(number, pin)
print("\nBalance: ₹" + str(atm.balance))

while True:
    choice = input("\nEnter choice: Withdrawl / Deposit / Check Balance / Exit: ")
    if choice == "Withdrawl":
        amt = int(input("Enter Amount: ₹"))    
        if atm.balance >= amt:
            atm.withdrawl(amt)
            print("Success!\n\nBalance: ₹" + str(atm.balance))
        else:
            print("You do not have that much money in your account.\n\nBalance: ₹" + str(atm.balance))

    elif choice == "Deposit":
        amt = int(input("Enter Amount: ₹"))    
        if amt > 0:
            atm.deposit(amt)
            print("Success!\n\nBalance: ₹" + str(atm.balance))
        else:
            print("Invalid Amount!\n\nBalance: ₹" + str(atm.balance))

    elif choice == "Check Balance":
        print("\nBalance: ₹" + str(atm.balance))

    elif choice == "Exit":
        break

    else:
        print("Invalid Option!")
