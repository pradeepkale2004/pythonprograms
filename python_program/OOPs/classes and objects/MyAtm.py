class MyAtm:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        print('''please Enter the valid input
                 1. Press 1 to create the new pin
                 2. Press 2 to update the pin
                 3. Press 3 to check the balance
                 4. Press 4 to withdraw the cash
                 0. Press 0 for Exit''')

        choice = int(input())
        if choice == 1:
            self.creating_pin()
        elif choice == 2:
            print('Updating new pin')
            self.update_pin()
        elif choice == 3:
            print('Checking Balance')
            self.balance_check()
        elif choice == 4:
            print('Withdrawing the cash')
            self.withdraw_cash()

    def creating_pin(self):
        if self.pin =='':
            try:
                new_pin = int(input("Enter the new pin to create"))
                if 3< len(str(abs(new_pin))) < 5:
                    self.pin = new_pin
                    self.balance = int(input('Enter the balance'))
                    print('Pin created successfully')
                    self.menu()
                else:
                    print('Enter the 4 digit pin')
                    self.creating_pin()
            except ValueError :
                print("Invalid input please enter in integer format")
                self.creating_pin()
        else:
            print('User already exist')

    def update_pin(self):
        self.old_pin = int(input('Enter the old pin'))
        if self.old_pin == self.pin:
            self.pin = int(input('Enter the new pin'))            
            print('Pin updated successfully')
        else:
            print('Enter correct old pin')
            self.update_pin()
        self.menu()

    def balance_check(self):
        pin_to_check_balance = int(input('Enter the pin to check the balance'))
        if pin_to_check_balance == self.pin:
            print(f'Current Balance is {self.balance}')
        else:
            print('Invalid pin! please enter correct pin')
            self.balance_check()
        self.menu()

    def withdraw_cash(self):
        pint_for_withdraw = int(input('Enter the pin'))
        if pint_for_withdraw == self.pin:
            amount_to_withdraw = int(input('Enter the amount to be withdraw'))
            if amount_to_withdraw < self.balance:
                remaining_balance = self.balance - amount_to_withdraw
                self.balance = remaining_balance
                print(f'Remaining balance is{self.balance}')
            else:
                print("insufficient balance")
        else:
            print('Incorrect pin! Please enter valid pin')
            self.withdraw_cash()
        self.menu()

a1 = MyAtm()