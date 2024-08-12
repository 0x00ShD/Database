class Loan:
  def __init__(self,id ,type , amount ,customer_id):
   self.id = id
   self.type = type
   self.amount = amount
   self.customer_id = customer_id

import sqlite3
myDB = sqlite3.connect("MYDATABASE.db")
cursor = myDB.cursor()


def get_loan_num():
  loan_id = input("Enter Loan ID")
  loan_id.strip()
  loan_id = int(loan_id)
  return loan_id

def is_loan_num_exist(loan_id):
    cursor.execute(f"SELECT * FROM LAONS WHERE LOANNUMBER = {loan_id}")
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False

# this assumes that informations is correct like SSN , Employee ID, branch ID and loan_num mustn't be exist before
def request_loan(loan_num,branch_id,loan_type,loan_amount,customer_id,employee_id):
    cursor.execute(f"INSERT INTO LAONS(LOANNUMBER,BRANCHNUMBER,LOANAMOUNT,LAONTYPE,STATUS) VALUES({loan_num},{branch_id},{loan_amount},'{loan_type}','Pending')") 
    myDB.commit()
    cursor.execute(f"INSERT INTO TAKE VALUES({customer_id},{loan_num})")
    myDB.commit()
    cursor.execute(f"INSERT INTO MANGE VALUES({employee_id},{loan_num})")
    myDB.commit()