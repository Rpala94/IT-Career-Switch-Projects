import logging
import random
import sys

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('formatted.log')

formatter = logging.Formatter('%(asctime)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")
    
  def authenticate(self):
    while True:
      pin = int(input("Enter account pin: "))
      if pin != 1234:
        print("Error! Invalid pin. Try again.")
      else:
        return None
 
  def deposit(self):
    try:
      amount=float(input("Enter amount to be deposited: "))
      if amount < 0:
        print("Warning! You entered a negative number to deposit.")
      self.balance += amount
      print("Amount Deposited: ${amount}".format(amount=amount))
      print("Transaction Info:")
      print("Status: Successful")
      print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      print("Timestamp: {timestamp}".format(timestamp=datetime.now()))
    except ValueError:
      print("Error! You entered a non-number value to deposit.")
      print("Transaction Info:")
      print("Status: Failed")
      print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      print("Timestamp: {timestamp}".format(timestamp=datetime.now()))
 
  def withdraw(self):
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      if self.balance >= amount:
        self.balance -= amount
        print("You withdrew: ${amount}".format( amount=amount))
        print("Transaction Info:")
        print("Status: Successful")
        print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      else:
        print("Error! Insufficient balance to complete withdraw.")
        print("Transaction Info:")
        print("Status: Failed")
        print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      print("Error! You entered a non-number value to withdraw.")
      print("Transaction Info:")
      print("Status: Failed")
      print("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      print("Timestamp: {timestamp}".format(timestamp=datetime.now()))
 
  def display(self):
    print("Available Balance = ${balance}".format(balance=self.balance))
 
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()