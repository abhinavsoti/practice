mydict = {}


class Account():

    def __init__(self, owner, balance):
        with open("AllAccount.txt") as f:
            for line in f:
                (key, val) = line.split('|')
                mydict[key] = int(val)

        self.owner = owner
        self.balance = balance
        mydict[self.owner] = self.balance

    def deposit(self, owner, amount):
        self.owner = owner
        self.amount = amount

        if self.owner in mydict.keys():
            currbal = mydict[self.owner]
            self.balance = currbal + self.amount
            mydict[self.owner] = self.balance
            print("Added " + str(self.amount) + " to your balance successfully")
        else:
            print('Account Not found, Please enter correct account owner name')

    def withdraw(self, owner, amount):

        self.owner = owner
        self.amount = amount

        if self.owner in mydict.keys():
            currbal = mydict[self.owner]

            if currbal >= self.amount:
                self.balance = currbal - self.amount
                mydict[self.owner] = self.balance
                print("Withdrawal Accepted")
                print("Your account balance is " + str(self.balance))
            else:
                print("Sorry!! Not enough funds in your account")
        else:
            print("You do not have account in our bank!!")

    def allaccounts(self):
        print('Owner | Balance')
        for i in mydict:
            print(i + ' | ' + str(mydict[i]))

    def allaccountsupdate(self):
        f = open('AllAccount.txt', 'w')
        for i in mydict:
            f.write(i + '|' + str(mydict[i]) + '\n')

        f.close()


    def __str__(self):
        return "Account Owner: " + str(self.owner) + "\n" + "Account Balance: " + str(self.balance)




# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit('Jose',50)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw('Jose', 500)

acct1.deposit('Jose',500)

acct2 = Account('Abhinav',100)

acct1.deposit('Abhinav',500)

acct2.withdraw('Jose', 75)

acct1.deposit('Abhinav',5000)

acct1.deposit('Jose',5000)

acct2.withdraw('Jose', 750)

acct2.withdraw('Abhinav', 850)

acct1 = Account('Saangvi',10000)

acct1.allaccounts()
acct1.allaccountsupdate()