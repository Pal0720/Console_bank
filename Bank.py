import random, sys, shelve

#Create the Bank class
class Bank:
    """Top class for storing bank details"""

    bank_name = "Reserve Bank of India"

    def __init__(self, branch):
        self.branch = branch


# Create the main user class
class User(Bank):
    """creates a user class for the bank, containing user details"""

#class variables
    total_accounts = 0
    all_details = []

    def __init__(self, name, acno):
        self.name = name
        self.acno = acno
        User.total_accounts += 1
        self.account_details = {}
        self.balance = 0

    def set_account(self, name, acno):
        """ Set details to 'account_details' list in a dictionary format"""
        self.account_details = {"Name":self.name,"Account_number" : self.acno, "Balance" : self.balance}
        User.all_details.append(self.account_details)


    def display_details(self, acno):
        """Display details based on account number"""
        print("For account number: {}\n Name : {}\t Bank balance: {} ".format(self.acno, self.name, self.balance))


    def deposit(self, amount):
        """Use this to deposit money in the account"""
        self.balance += amount
        print("Congrats amount deposited. Now total balance in account no {} is {}".format(self.acno,self.balance))


    def withdraw(self, amount):
        """Use this to withdraw money from the account"""
        if self.balance >= amount:
            self.balance -= amount
            print("Congrats amount withdrawn. Now total balance in account no {} is {}".format(self.acno,self.balance))
        else:
            print("Sorry...Funds not available..!")


    def minimum_balance(self):
        """Use this to check if there is minimum balance in the account"""
        if self.balance<100:
            print("Amount less than minimum balance, please deposit funds")
        else:
            print("{} Rs. to go for minimum balance".format(self.balance - 100))


##########################################################################################
# program start

print("Hello, welcome to {}!!".format(Bank.bank_name))
print("Open a savings account and get the best interest rates")

print()

#create a list to store all the User objects.
user_objects = []

while(True):
    print("--------------------------------------------------------------------")
    print()
    choice = str(input("Enter a choice (1-7) : \n1) Open an account \n2) Check account details \n3) See all accounts \n4) Check minimum balance accounts \n5) Deposit money \n6) Withdraw money \n7) Check total number of accounts : \n8) Exit : \n"))

    print()

    if choice == '1':
        print("\nProceed to open an account...")
        name = str(input("Enter your name : "))
        account_num = random.randint(100000,999999)
        #create user
        user_objects.append(User(name,account_num))
        user_objects[-1].set_account(name, account_num)
        print("Congratulations.. Your account opened in {}.\n Your details are {}".format(Bank.bank_name,user_objects[-1].account_details))


    elif choice == '2':
        check_ac_num = int(input("Enter account number to check details : "))
        for i in user_objects:
            if i.acno == check_ac_num:
                i.display_details(i.acno)
                break
        else:
            print("Account number doesnt exist")


    elif choice == '3':
        for i in User.all_details:
            print(i)  ####


    elif choice == '4':
        str_input = str(input("Do you want to see all accounts with minimum balance or check an account? Write all or one : "))
        if str_input == 'all':
            for i in user_objects:
                print("For account number: {} Name: {}".format(i.acno,i.name))
                i.minimum_balance()
        elif str_input == 'one':
            account_num = int(input("Enter the account number for which you want to check : "))
            for i in user_objects:
                if i.acno == account_num:
                    i.minimum_balance()
                    break
            else:
                print("Invald account number... Please retry")
        else:
            print("Invalid input.. Retry")


    elif choice == '5':
        account_num = int(input("Enter the account number for which you want to deposit : "))
        amount = int(input("Enter the amount you want to deposit : "))
        for i in user_objects:
            if i.acno == account_num:
                i.deposit(amount)
                i.account_details['Balance'] = i.balance
                break
        else:
            print("Invalid input.. Retry")


    elif choice == '6':
        account_num = int(input("Enter the account number for which you want to withdraw : "))
        amount = int(input("Enter the amount you want to withdraw : "))
        for i in user_objects:
            if i.acno == account_num:
                i.withdraw(amount)
                i.account_details['Balance'] = i.balance
                break
        else:
            print("Invalid input.. Retry")


    elif choice == '7':
        print("Total number of accounts in this branch are : {}".format(User.total_accounts))


    elif choice == '8':
        print("Thankyou. Visit again...!!")
        sys.exit()

    else:
        print("Invalid entry... Try again")
