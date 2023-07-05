class user:
  
  # Constructor
  def __init__ (self, username, password, accountHolder, accountNumber, balance):
    self.username = username
    self.password = password
    self.accountHolder = accountHolder
    self.accountNumber = accountNumber
    self.balance = balance

  # Getters and setters
  
  # Getter
  def getUserName(self):
    return self.username

  # Setter
  def setUserName(self, newUserName):
    self.username = newUserName

  def getPassword(self):
    return self.password

  def setPassword(self, newPassword):
    self.password = newPassword

  def getAccountHolder(self):
    return self.accountHolder

  def setAccountHolder(self, newAccountHolder):
    self.accountHolder = newAccountHolder

  def getAccountNumber(self):
    return self.accountNumber

  def setAccountNumber(self, newAccountNumber):
    self.accountHolder = newAccountNumber

  def getAccountBalance(self):
    return self.balance

  def setAccountBalance(self, deposit):
    self.balance = self.balance+deposit

  def withdraw(self, withdrawAmount):
    if withdrawAmount < 0:
      return "cannot withdraw a negative amount!"
    elif self.balance < withdrawAmount:
      return "insufficient funds"
    else:
      self.balance = self.balance - withdrawAmount
  