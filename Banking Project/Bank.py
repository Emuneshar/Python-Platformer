import random
import os 
from user import user

print("Welcome to the bank!\n")
print("What would you like to do? Your options are\n",
        "1. Open an Account\n",
        "2. Deposit Money\n",
        "3. Withdraw Money\n",
        "4. View Balance\n",
        "5. Close Account\n")

choice = int(input("What would you like to do?\n"))

listOfAccounts = []

def createAccount():
  User = user(username = "", password = "", accountHolder = "", accountNumber = 0, balance = 0)
  userN = str(input("Whats your name?\n"))
  passW = str(input("Please enter a password\n"))
  accountH = str(input("What is your full name?\n"))
  accountN = random.randint(999999,999999999)
  bal = random.randint(0,10000000000)
  User.setUserName(userN)
  User.setPassword(passW)
  User.setAccountHolder(accountH)
  User.setAccountNumber(accountN)
  User.setAccountBalance(bal)
  return User  
  

while True:
  
  choice = int(input("What would you like to do?\n"))
  
  match choice:
    case 1:
      listOfAccounts.append(createAccount())
      
    case 2:
      userName = input("What is your username?")
      for x in listOfAccounts:
        if x.getUserName() == userName:
            print("We found your account!")
            password = input("Please enter the password for your account:\n ")
            if x.getPassword() == password:
                print("You're in!")
                deposit = float(input("How much would you like to deposit?"))
                x.setAccountBalance(x.getAccountBalance()+deposit)
                






