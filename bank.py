class Atm():
    def __init__(self,last4, pin, balance=0):
        self.last4 = last4
        self.pin = pin
        self.balance = balance
    def validate_access(self, last4, pin):
        if last4 == self.last4 and pin == self.pin:
            return True
        else:
            return False
    def check_balance(self):
        return self.balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return self.balance
    def change_password(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
            return "updated"

user_accounts = {}

##New ATM user registration section
def register_user():
    last4 = input("Enter your card's last 4 number: ")
    pin = input("Enter your new pin: ")
    balance = int(input("Please deposite initial amount: "))
    if balance < 0:
        print("Invalid amount")
        return
    if len(str(pin)) != 4 or not pin.isdigit():
        print("Invalid pin")
        return
    if last4 in user_accounts:
        print("User already exists")
        return
    user_accounts[last4] = Atm(last4, pin, balance)
    print("Your account has been created")

## welcome page

while True:
    print("1. Register new user")
    print("2. Login")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        register_user()
    elif choice == 2:
        last4 = input("Enter your card's last 4 number: ")
        pin = input("Enter your pin: ")
        if last4 in user_accounts and user_accounts[last4].validate_access(last4, pin):
            atm = user_accounts[last4]
            while True:
                print("Welcome")
                print("Your balance is: ", atm.check_balance())
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Change pin")
                print("4. Exit")
                user_choice = int(input("Enter your choice: "))
                if user_choice == 1:
                    atm.deposit(int(input("Enter amount to deposit: ")))
                elif user_choice == 2:
                    atm.withdraw(int(input("please enter the amount to withdraw: ")))
                elif user_choice == 3:
                    atm.change_password(input("enter the new pin: "))
                elif user_choice == 4:
                    print("Thank you")
                    break
        else:
            print("Wrong card number or pin")
            break
    else:
        print("Invalid choice")

        