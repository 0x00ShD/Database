class customer:
  def __init__(self,SSN ,CUSTOMERNAME , CUSTOMERADDRESS,CUSTOMERPHONE,BRANCHNUMBER):
    self.SSN =SSN
    self.CUSTOMERNAME=CUSTOMERNAME
    self.CUSTOMERADDRESS = CUSTOMERADDRESS
    self.CUSTOMERPHONE=CUSTOMERPHONE
    self.BRANCHNUMBER = BRANCHNUMBER



import sqlite3
myDB = sqlite3.connect("MYDATABASE.db")
cursor = myDB.cursor()
def new_Customer():
  id =input("Enter your id: ")
  cursor.execute(f"select * from CUSTOMER where SSN ={id}")
  if(len(cursor.fetchall())==1):
   print("This id Exist!!")
   new_Customer()  
   
  name =input("Enter your Name: ")
  cursor.execute(f"select * from CUSTOMER where CUSTOMERNAME ='{name}'")
  if(len(cursor.fetchall())==1):
   print("This Name Exist!!")
   new_Customer()  
  address = input("Enter your Address: ")
  cursor.execute(f"select * from CUSTOMER where CUSTOMERADDRESS ='{address}'")
  phone = input("Enter your phone: ")
  cursor.execute(f"select * from CUSTOMER where CUSTOMERPHONE ='{phone}'")
  if(len(cursor.fetchall())==1):
    print("This phone Exist!!")
    new_Customer()
  code = input("Enter Branch id: ")
  cursor.execute(f"select * from BRANCH where BRANCHNUMBER ={code}")
  if(len(cursor.fetchall())!=1):
    print("this Branch not exist!!")
    new_Customer()
  NewObj = customer(id,name ,address,phone,code)
  cursor.execute(f"insert into CUSTOMER values({NewObj.SSN},{NewObj.BRANCHNUMBER},'{NewObj.CUSTOMERNAME}','{NewObj.CUSTOMERPHONE}','{NewObj.CUSTOMERADDRESS}')")
  print("operation done successfull")
  myDB.commit() 

def getSSN():
    SSN = input("Enter Your SSN: ")
    return SSN
  
def check_SSN(SSN):
  cursor.execute(f"SELECT SSN FROM CUSTOMER WHERE SSN = {SSN}")
  result = cursor.fetchone()
  if result:
    return True
  else:
    return False

def change_SSN(SSN):
    new_ssn = input("Enter the New SSN: ")
    cursor.execute(f"UPDATE CUSTOMER SET SSN = {new_ssn} WHERE SSN = {(SSN)}").fetchone()
    myDB.commit()
    if(cursor.rowcount > 0):
      print("SSN has changed successfully")
    else:
      print("SSN you have entered isn't exist or maybe SSN you wanna change to is ")


def change_branch(SSN):
  new_branch = input("Enter The new Branch ")
  cursor.execute(f"UPDATE CUSTOMER SET BRANCHNUMBER = {new_branch} where SSN = {SSN}")
  myDB.commit()
  if cursor.rowcount > 0:
    print(" Change Updated Successfully")
  else:
    print("Branch is not exist in Branch Table")

def change_name(SSN):
  new_name = input("Enter The New Name ")
  cursor.execute(f"UPDATE CUSTOMER SET CUSTOMERNAME = '{new_name}' where SSN = {SSN}")
  myDB.commit()
  if cursor.rowcount > 0:
    print(" Change Updated Successfully")
  else:
    print(" Change hasn't done, There's an error ")
    
def change_phone(SSN):
  new_phone = input("Enter The new phone ")
  cursor.execute(f"UPDATE CUSTOMER SET CUSTOMERPHONE = {new_phone} where SSN = {SSN}")
  myDB.commit()

  if cursor.rowcount > 0:
    print(" Change Updated Successfully")
  else:
    print(" Change hasn't done, There's an error ")
    
def change_address(SSN):
  new_address = input("Enter your New Address")
  cursor.execute(f"UPDATE CUSTOMER SET CUSTOMERADDRESS = {new_address} where SSN = {SSN}")
  myDB.commit()

  if cursor.rowcount > 0:
      print("Change Updated Successfully")
  else:
      print("The SSN provided isn't correct")
      newSSN = getSSN()
      change_address(newSSN)

def returnSSNResult():
  SSN = getSSN()
  SSN.strip()
  SSN = int(SSN)
  if(check_SSN(SSN)):
    cursor.execute(f"SELECT * from CUSTOMER WHERE SSN = {SSN}")
    customer_data = cursor.fetchone()
    return customer_data,SSN
  else:
    print("Customer with the provided SSN does not exist.")
    returnSSNResult()