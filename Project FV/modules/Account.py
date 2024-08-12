class Account:
  def __init__(self, SSN, ACCOUNTNUMBER,ACCOUNTTYPE,BALANCE):
    self.SSN = SSN
    self.ACCOUNTNUMBER = ACCOUNTNUMBER
    self.ACCOUNTTYPE = ACCOUNTTYPE
    self.BALANCE = BALANCE
import sqlite3
myDB = sqlite3.connect("MYDATABASE.db")
cursor = myDB.cursor()

def get_account_num():
  account_num = input("Enter Account Number ")
  account_num.strip()
  account_num = int(account_num)
  return account_num

def check_account_number(account_num):
  cursor.execute(f"Select * from ACCOUNT WHERE ACCOUNTNUMBER = {account_num}")
  result = cursor.fetchone()
  if result:
    return True
  else:
    return False
  
def return_account_num_data():
  account_num = get_account_num()
  is_valid_account = check_account_number(account_num)
  if is_valid_account:
    return account_num
  else:
    print("Account Number you have entered isn't exist")
    return_account_num_data()
def change_account_num():
    account_num = get_account_num()
    if(check_account_number(account_num)):
      new_account_num = input("Enter the New Account Number: ")
      new_account_num.strip()
      new_account_num = int(new_account_num)    
      cursor.execute(f"UPDATE ACCOUNT SET ACCOUNTNUMBER = {new_account_num} WHERE ACCOUNTNUMBER = {account_num}")
      myDB.commit()
      
      if cursor.rowcount > 0:
          print("Account Number has been changed successfully.")
      else:
          print("Failed to change the Account Number.")
    else:
      print("Account Number Entered isn't exist please try again")
      change_account_num()
      
# pre-condition : function assumes that account_num is exist in database
def get_balance(account_num):
  cursor.execute(f"SELECT BALANCE FROM ACCOUNT WHERE ACCOUNTNUMBER = {account_num}")
  result = cursor.fetchone()
  balance = result[0]
  return balance