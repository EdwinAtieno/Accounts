class Accounts:
    def __init__(self):
        # wanjiru's account
        self.Wanjiru_account = 0

        # Juma's account
        self.Juma_account = 0

        # Linda's account
        self.Linda_account = 0

        print("Welcome to our banking system")
    #deposit function
    def deposit(self):
        # check who is making the deposit
        if self.name == "wanjiru":
            amount = float(input("Enter amount to be Deposited: "))

            # Credit wanjiru's account
            self.Wanjiru_account += amount
            print("\n Amount Deposited:\t", amount)

        # check who is making the deposit
        elif self.name == "juma":
            amount = float(input("Enter amount to be Deposited:\t"))

            # Credit Juma's account
            self.Juma_account += amount
            print("\n Amount Deposited:\t", amount)

        # check who is making the deposit
        else:
            amount = float(input("Enter amount to be Deposited:\t"))

            # Credit Linda's account
            self.Linda_account += amount
            print("\n Amount Deposited:\t", amount)

    """ check if the user has any amount in their accounts and verify who is doing the withdrawal before making the withdrawal
            from their account and the return insufficient message if account is less"""
    def withdraw(self):

        if self.name == "wanjiru":
            amount = float(input("Enter amount to be Withdrawn:\t"))
            if self.Wanjiru_account >= amount:
                self.Wanjiru_account -= amount
                print("\n You Withdrew:\t", amount)
            else:
                print("\n Insufficient balance")

        elif self.name == "juma":
            amount = float(input("Enter amount to be Withdrawn:\t"))
            if self.Juma_account >= amount:
                self.Juma_account -= amount
                print("\n You Withdrew:\t", amount)
            else:
                print("\n Insufficient balance")

        else:
            amount = float(input("Enter amount to be Withdrawn:\t"))

            if self.Linda_account >= amount:
                self.Linda_account -= amount
                print("\n You Withdrew:\t", amount)

            else:
                print("\n Insufficient balance")

    """Bank transfer for customers depending on the account balance"""
    def transfer(self):
        if self.name == "wanjiru":
            amount = float(input("Enter amount to be transfer:\t"))

            transferee= str(input("enter user to send to, Linda or Juma\t")).lower()

            if self.Wanjiru_account >= amount:
                self.Wanjiru_account -= amount

                if transferee == "juma":
                    self.Juma_account += amount

                elif transferee == "linda":
                    self.Linda_account += amount

                print("\n You transferred:\t", amount)
            else:
                print("\n Insufficient balance  ")

        elif self.name == "Juma":
            amount = float(input("Enter amount to be transfer:\t"))

            transferee = str(input("enter user to send to, wanjiru or Linda:\t")).lower()

            if self.Juma_account >= amount:
                self.Juma_account -= amount

                if transferee == "wanjiru":
                    self.Wanjiru_account += amount

                elif transferee == "linda":
                    self.Linda_account += amount
                print("\n You transferred:\t", amount)

            else:
                print("\n Insufficient balance  ")

        else:
            amount = float(input("Enter amount to be transfer:\t"))

            transferee = str(input("enter user to send to, wanjiru or Juma:\t")).lower()

            if self.Linda_account >= amount:
                self.Linda_account -= amount

                if transferee == "juma":
                    self.Juma_account += amount

                elif transferee == "wanjiru":
                    self.Wanjiru_account += amount

                print("\n You transferred\t:", amount)

            else:
                print("\n Insufficient balance  ")



    def display(self):
        if self.name == "wanjiru":
            print("\n Net Available Balance=", self.Wanjiru_account)
        elif self.name == "juma":
            print("\n Net Available Balance=", self.Juma_account)
        else:
            print("\n Net Available Balance=", self.Linda_account)

    def credentials(self):
        while True:
            self.name= str(input("please enter you name of customer to continue (Wanjiru, Juma, Linda): ")).lower()
            if self.name == "wanjiru":
                print("\n your account ballance is:", self.Wanjiru_account)
                service = int(input("Please select service: 1=Deposit\n 2=Withdraw\n 3=Transfer:  "))
                if service ==1:
                    self.deposit()
                elif service ==2:
                    self.withdraw()
                elif service ==3:
                    self.transfer()
                else:
                    print("you have entered wrong value")
                self.display()

            elif self.name == "juma":
                print("\n your account ballance is:", self.Juma_account)
                service = int(input("Please select service: 1=Deposit\n 2=Withdraw\n 3=Transfer:  "))
                if service == 1:
                    self.deposit()
                elif service == 2:
                    self.withdraw()
                elif service == 3:
                    self.transfer()
                else:
                    print("you have entered wrong value")

                self.display()

            elif self.name == "linda":
                print("\n your account ballance is:", self.Linda_account)
                service = int(input("Please select service: 1=Deposit\n 2=Withdraw\n 3=Transfer:  "))
                if service == 1:
                    self.deposit()
                elif service == 2:
                    self.withdraw()
                elif service == 3:
                    self.transfer()
                else:
                    print("you have entered wrong value")
                self.display()

            final_procedure = str(input("are you done, Yes or No\n")).lower()
            if final_procedure == "yes":
                break

# Driver code

# creating an object of class
transact = Accounts()

# Calling functions with that class object
transact.credentials()

