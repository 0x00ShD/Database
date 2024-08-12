from modules import Bank, Account, Branch, customer, Loan, worker
import sqlite3

myDB = sqlite3.connect("MYDATABASE.db")
cursor = myDB.cursor()

print("1- login as admin ")
print("2- login as employee ")
print("3- login as customer ")
choice = input("enter choice: ")

if choice == "1":
    print("\
        1- add new bank \
        2- add new branch \
        3- add new employee admin \
        ")
    ch = input("enter your choice: ")
    if ch == "1":
        Bank.new_Bank()
    elif ch == "2":
        Branch.new_Branch()
    elif ch == "3":
        worker.new_Employee()

elif choice == "2":
    print("\
        1- add new customer\
        ")
    cf = input("enter your choice: ")
    if cf == "1":
        customer.new_Customer()
elif choice == "3":
    print("\
        1- update data \
        2- show balance \
        3- request loan \
        ")
    ch = input("enter your choice: ")
    if ch == "1":
        customer_data ,SSN = customer.returnSSNResult()
        print(customer_data)
        change_data_choice = input("Choose from List what data you would like to change \n \
                            1- SSN \n \
                            2- Branch Number\n \
                            3- Customer Name\n \
                            4- Customer Phone\n \
                            5- Customer Address\n \
                            ")
        if change_data_choice == "1":
            customer.change_SSN(SSN)
        elif change_data_choice == "2":
            customer.change_branch(SSN)
        elif change_data_choice == "3":
            customer.change_name(SSN)
        elif change_data_choice == "4":
            customer.change_name(SSN)
        elif change_data_choice == "5":
            customer.change_address(SSN)
    elif ch == "2":
      account_num = Account.return_account_num_data()
      print(Account.get_balance(account_num))
    elif ch == "3":
        loan_amount = input("Enter the loan amount")
        while(True):
         branch_num = Branch.get_branch_num()
         if Branch.is_branch_exist(branch_num):    
            loan_type = input("Enter Loan type (e.g. industry loan, commercial loan, Personal loan")
            loan_num =  Loan.get_loan_num()
            if Loan.is_loan_num_exist(loan_num):
               print("Loan Number Exist")
            else:
               SSN = customer.getSSN()
               if(customer.check_SSN(SSN)):
                  employee_id = worker.get_employee_id()
                  if worker.check_employee_exist(employee_id):
                     Loan.request_loan(loan_num,branch_num,loan_type,loan_num,SSN,employee_id)
                     print("Loan has inserted successfully")
                  else:
                     print("Employee ID isn't exist")
               else:
                  print("SSN isn't exist")
