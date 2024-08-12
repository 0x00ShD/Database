# Description: This file contains the code for the GUI of the Bank Database Management System
from tkinter import *
from modules import Bank, Account, Branch, customer, Loan, worker
import sqlite3
from PIL import ImageTk, Image


# Create a connection to the database
myDB = sqlite3.connect("MYDATABASE.db")
cursor = myDB.cursor()

# Create the main application window
root = Tk()
root.title("Bank Database Management System")
root.geometry("500x500")
root.config(bg="white")
root.config(highlightcolor="green")
root.config(highlightthickness=10)
root.config(borderwidth=5)
root.config(relief="solid")
root.config(cursor="arrow")
root.config(height=3)
root.config(width=20)


# Function to handle the admin login
def admin_login():
    admin_window = Toplevel(root)
    admin_window.title("Admin Login")
    admin_window.geometry("1070x690")

    # Function to handle adding a new bank
    def add_bank():
        def submit():

            myDB = sqlite3.connect("MYDATABASE.db")
            cursor = myDB.cursor()

            cursor.execute("INSERT INTO BANK VALUES (:BANKCODE, :BANKNAME, :BANKADDRESS)",
            {
                'BANKCODE':BANKCODE.get(),
                'BANKNAME':BANKNAME.get(),
                'BANKADDRESS':BANKADDRESS.get(),
            })

            BANKCODE.delete(0, END)
            BANKNAME.delete(0,END)
            BANKADDRESS.delete(0,END)

            myDB.commit()
            myDB.close()

        add_bank_window = Toplevel(admin_window)
        add_bank_window.title("Add New Bank")

        
        BANKCODE = Entry(add_bank_window,width=30,borderwidth=5)
        BANKCODE.grid(row=0,column=1,padx=20,pady=(10,0))

        BANKNAME = Entry(add_bank_window,width=30,borderwidth=5)
        BANKNAME.grid(row=1,column=1,padx=20)

        BANKADDRESS = Entry(add_bank_window,width=30,borderwidth=5)
        BANKADDRESS.grid(row=2,column=1,padx=20)

        BANKCODE_label = Label(add_bank_window,text="BANKCODE")
        BANKCODE_label.grid(row=0,column=0,pady=(10,0))

        BANKNAME_label = Label(add_bank_window,text="BANKNAME")
        BANKNAME_label.grid(row=1,column=0)

        BANKADDRESS_label = Label(add_bank_window,text="BANKADDRESS")
        BANKADDRESS_label.grid(row=2,column=0)


        submit_btn = Button(add_bank_window,text="Add Record To Database",command=submit)
        submit_btn.grid(row=3,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

     
    def add_branch():
        def submit():

            myDB = sqlite3.connect("MYDATABASE.db")
            cursor = myDB.cursor()

            cursor.execute("INSERT INTO BRANCH VALUES (:BRANCHNUM, :BRANCHNAME, :BRANCHADDRESS, :BANKCODE)",
            {
                'BRANCHNUM':BRANCHNUM.get(),
                'BRANCHNAME':BRANCHNAME.get(),
                'BRANCHADDRESS':BRANCHADDRESS.get(),
                'BANKCODE':BANKCODE.get(),
            })

            BRANCHNUM.delete(0, END)
            BRANCHNAME.delete(0,END)
            BRANCHADDRESS.delete(0,END)
            BANKCODE.delete(0,END)

            myDB.commit()
            myDB.close()


        add_branch_window = Toplevel(admin_window)
        add_branch_window.title("Add New Branch")

        BRANCHNUM = Entry(add_branch_window,width=30,borderwidth=5)
        BRANCHNUM.grid(row=0,column=1,padx=20,pady=(10,0))

        BRANCHNAME = Entry(add_branch_window,width=30,borderwidth=5)
        BRANCHNAME.grid(row=1,column=1,padx=20)

        BRANCHADDRESS = Entry(add_branch_window,width=30,borderwidth=5)
        BRANCHADDRESS.grid(row=2,column=1,padx=20)

        BANKCODE = Entry(add_branch_window,width=30,borderwidth=5)
        BANKCODE.grid(row=3,column=1,padx=20)

        BRANCHNUM_label = Label(add_branch_window,text="BRANCHNUM")
        BRANCHNUM_label.grid(row=0,column=0,pady=(10,0))

        BRANCHNAME_label = Label(add_branch_window,text="BRANCHNAME")
        BRANCHNAME_label.grid(row=1,column=0)

        BRANCHADDRESS_label = Label(add_branch_window,text="BRANCHADDRESS")
        BRANCHADDRESS_label.grid(row=2,column=0)

        BANKCODE_label = Label(add_branch_window,text="BANKCODE")
        BANKCODE_label.grid(row=3,column=0)

        submit_btn = Button(add_branch_window,text="Add Record To Database",command=submit)
        submit_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=100)


        Branch.new_Branch()

    def add_employee():
        def submit():
            myDB = sqlite3.connect("MYDATABASE.db")
            cursor = myDB.cursor()

            cursor.execute("INSERT INTO WORKER VALUES (:EMPLOYEEID, :EMPLOYEENAME, :EMPLOYEEPHONE, :EMPLOYEEADDRESS, :BRANCHNUM)",
            {
                'EMPLOYEEID':EMPLOYEEID.get(),
                'EMPLOYEENAME':EMPLOYEENAME.get(),
                'EMPLOYEEPHONE':EMPLOYEEPHONE.get(),
                'EMPLOYEEADDRESS':EMPLOYEEADDRESS.get(),
                'BRANCHNUM':BRANCHNUM.get(),
            })

            EMPLOYEEID.delete(0, END)
            EMPLOYEENAME.delete(0,END)
            EMPLOYEEPHONE.delete(0,END)
            EMPLOYEEADDRESS.delete(0,END)
            BRANCHNUM.delete(0,END)

            myDB.commit()
            myDB.close()
        add_employee_window = Toplevel(admin_window)
        add_employee_window.title("Add New Employee")

        EMPLOYEEID = Entry(add_employee_window,width=30,borderwidth=5)
        EMPLOYEEID.grid(row=0,column=1,padx=20,pady=(10,0))

        EMPLOYEENAME = Entry(add_employee_window,width=30,borderwidth=5)
        EMPLOYEENAME.grid(row=1,column=1,padx=20)

        EMPLOYEEPHONE = Entry(add_employee_window,width=30,borderwidth=5)
        EMPLOYEEPHONE.grid(row=2,column=1,padx=20)

        EMPLOYEEADDRESS = Entry(add_employee_window,width=30,borderwidth=5)
        EMPLOYEEADDRESS.grid(row=3,column=1,padx=20)

        BRANCHNUM = Entry(add_employee_window,width=30,borderwidth=5)
        BRANCHNUM.grid(row=4,column=1,padx=20)

        EMPLOYEEID_label = Label(add_employee_window,text="EMPLOYEEID")
        EMPLOYEEID_label.grid(row=0,column=0,pady=(10,0))

        EMPLOYEENAME_label = Label(add_employee_window,text="EMPLOYEENAME")
        EMPLOYEENAME_label.grid(row=1,column=0)

        EMPLOYEEPHONE_label = Label(add_employee_window,text="EMPLOYEEPHONE")
        EMPLOYEEPHONE_label.grid(row=2,column=0)

        EMPLOYEEADDRESS_label = Label(add_employee_window,text="EMPLOYEEADDRESS")
        EMPLOYEEADDRESS_label.grid(row=3,column=0)

        BRANCHNUM_label = Label(add_employee_window,text="BRANCHNUM")
        BRANCHNUM_label.grid(row=4,column=0)

        submit_btn = Button(add_employee_window,text="Add Record To Database",command=submit)
        submit_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

        worker.new_Employee()

    # Create buttons for admin actions
    bank_btn = Button(admin_window, text="Add New Bank", command=add_bank)

    branch_btn = Button(admin_window, text="Add New Branch", command=add_branch)

    employee_btn = Button(admin_window, text="Add New Employee", command=add_employee)

    bank_btn.grid(row=2, column=0)
    bank_btn.config(font=("Pacifico",20))
    bank_btn.config(anchor=CENTER)
    bank_btn.config(wraplength=500)
    bank_btn.config(bg="white")
    bank_btn.config(fg="red")
    bank_btn.config(height=20)
    bank_btn.config(width=20)
    bank_btn.config(relief="solid")
    bank_btn.config(borderwidth=5)
    bank_btn.config(highlightcolor="green")
    bank_btn.config(highlightthickness=10)
    
    branch_btn.grid(row=2, column=1)
    branch_btn.config(font=("Pacifico",20))
    branch_btn.config(anchor=CENTER)
    branch_btn.config(wraplength=500)
    branch_btn.config(bg="white")
    branch_btn.config(fg="green")
    branch_btn.config(height=20)
    branch_btn.config(width=20)
    branch_btn.config(relief="solid")
    branch_btn.config(borderwidth=5)
    branch_btn.config(highlightcolor="green")
    branch_btn.config(highlightthickness=10)

    employee_btn.grid(row=2, column=2)
    employee_btn.config(font=("Pacifico",20))
    employee_btn.config(anchor=CENTER)
    employee_btn.config(wraplength=500)
    employee_btn.config(bg="white")
    employee_btn.config(fg="blue")
    employee_btn.config(height=20)
    employee_btn.config(width=20)
    employee_btn.config(relief="solid")
    employee_btn.config(borderwidth=5)
    employee_btn.config(highlightcolor="green")
    employee_btn.config(highlightthickness=10)



# Function to handle the employee login
def employee_login():
    employee_window = Toplevel(root)
    employee_window.title("Employee Login")

    def add_customer():

        def submit():
            myDB = sqlite3.connect("MYDATABASE.db")
            cursor = myDB.cursor()

            cursor.execute("INSERT INTO CUSTOMER VALUES (:SSN, :CUSTOMERNAME, :CUSTOMERPHONE, :CUSTOMERADDRESS, :BRANCHNUM)",
            {
                'SSN':SSN.get(),
                'CUSTOMERNAME':CUSTOMERNAME.get(),
                'CUSTOMERPHONE':CUSTOMERPHONE.get(),
                'CUSTOMERADDRESS':CUSTOMERADDRESS.get(),
                'BRANCHNUM':BRANCHNUM.get(),
            })

            

            SSN.delete(0, END)
            CUSTOMERNAME.delete(0,END)
            CUSTOMERPHONE.delete(0,END)
            CUSTOMERADDRESS.delete(0,END)
            BRANCHNUM.delete(0,END)

            myDB.commit()
            myDB.close()
        
        add_customer_window = Toplevel(employee_window)
        add_customer_window.title("Add New Customer")

        SSN = Entry(add_customer_window,width=30,borderwidth=5)
        SSN.grid(row=0,column=1,padx=20,pady=(10,0))

        CUSTOMERNAME = Entry(add_customer_window,width=30,borderwidth=5)
        CUSTOMERNAME.grid(row=1,column=1,padx=20)

        CUSTOMERPHONE = Entry(add_customer_window,width=30,borderwidth=5)
        CUSTOMERPHONE.grid(row=2,column=1,padx=20)

        CUSTOMERADDRESS = Entry(add_customer_window,width=30,borderwidth=5)
        CUSTOMERADDRESS.grid(row=3,column=1,padx=20)

        BRANCHNUM = Entry(add_customer_window,width=30,borderwidth=5)
        BRANCHNUM.grid(row=4,column=1,padx=20)

        SSN_label = Label(add_customer_window,text="SSN")
        SSN_label.grid(row=0,column=0,pady=(10,0))

        CUSTOMERNAME_label = Label(add_customer_window,text="CUSTOMERNAME")
        CUSTOMERNAME_label.grid(row=1,column=0)

        CUSTOMERPHONE_label = Label(add_customer_window,text="CUSTOMERPHONE")
        CUSTOMERPHONE_label.grid(row=2,column=0)

        CUSTOMERADDRESS_label = Label(add_customer_window,text="CUSTOMERADDRESS")
        CUSTOMERADDRESS_label.grid(row=3,column=0)

        BRANCHNUM_label = Label(add_customer_window,text="BRANCHNUM")
        BRANCHNUM_label.grid(row=4,column=0)

        submit_btn = Button(add_customer_window,text="Add Record To Database",command=submit)
        submit_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
        # Add new customer logic here
        customer.new_Customer()

    # Create a button for adding a new customer
    customer_btn = Button(employee_window, text="Add New Customer", command=add_customer)
    customer_btn.grid(row=2, column=0)
    customer_btn.config(font=("Pacifico",20))
    customer_btn.config(anchor=CENTER)
    customer_btn.config(wraplength=500)
    customer_btn.config(bg="white")
    customer_btn.config(fg="red")
    customer_btn.config(height=20)
    customer_btn.config(width=20)
    customer_btn.config(relief="solid")
    customer_btn.config(borderwidth=5)
    customer_btn.config(highlightcolor="green")
    customer_btn.config(highlightthickness=10)
    customer_btn.pack()

# Function to handle the customer login
def customer_login():
    customer_window = Toplevel(root)
    customer_window.title("Customer Login")
    customer_window.geometry("1070x690")


    def update_data():
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
        # Update customer data logic here


    def show_balance():
        # Show customer balance logic here
        account_num = Account.return_account_num_data()
        print(Account.get_balance(account_num))

    def request_loan():
        # Request loan logic here
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

    # Create buttons for customer actions
    update_btn = Button(customer_window, text="Update Data", command=update_data)

    balance_btn = Button(customer_window, text="Show Balance", command=show_balance)

    loan_btn = Button(customer_window, text="Request Loan", command=request_loan)

    update_btn.grid(row=2, column=0)
    update_btn.config(font=("Pacifico",20))
    update_btn.config(anchor=CENTER)
    update_btn.config(wraplength=500)
    update_btn.config(bg="white")
    update_btn.config(fg="red")
    update_btn.config(height=20)
    update_btn.config(width=20)
    update_btn.config(relief="solid")
    update_btn.config(borderwidth=5)
    update_btn.config(highlightcolor="green")
    update_btn.config(highlightthickness=10)
    
    balance_btn.grid(row=2, column=1)
    balance_btn.config(font=("Pacifico",20))
    balance_btn.config(anchor=CENTER)
    balance_btn.config(wraplength=500)
    balance_btn.config(bg="white")
    balance_btn.config(fg="green")
    balance_btn.config(height=20)
    balance_btn.config(width=20)
    balance_btn.config(relief="solid")
    balance_btn.config(borderwidth=5)
    balance_btn.config(highlightcolor="green")
    balance_btn.config(highlightthickness=10)

    loan_btn.grid(row=2, column=2)
    loan_btn.config(font=("Pacifico",20))
    loan_btn.config(anchor=CENTER)
    loan_btn.config(wraplength=500)
    loan_btn.config(bg="white")
    loan_btn.config(fg="blue")
    loan_btn.config(height=20)
    loan_btn.config(width=20)
    loan_btn.config(relief="solid")
    loan_btn.config(borderwidth=5)
    loan_btn.config(highlightcolor="green")
    loan_btn.config(highlightthickness=10)


# Function to handle the login choice
def login_choice():
    choice = choice_entry.get()
    if choice == "admin":
        admin_login()
    elif choice == "employee":
        employee_login()
    elif choice == "customer":
        customer_login()

# Create the login screen
login_label = Label(root, text="Login as:")
login_label.config(font=("Helvetica","16"))
login_label.config(anchor=CENTER)
login_label.config(wraplength=500)
login_label.config(bg="white")
login_label.config(fg="black")
login_label.config(height=3)    
login_label.config(width=20)    
login_label.config(relief="solid")
login_label.config(borderwidth=5)   
login_label.config(highlightcolor="green")
login_label.config(highlightthickness=10)

login_label.pack()

choice_entry = Entry(root,width=30,borderwidth=5)
choice_entry.insert(0,"")
choice_entry.config(font=("Pacifico",20))
choice_entry.config(justify=CENTER)
choice_entry.config(bg="white")
choice_entry.config(fg="black")
choice_entry.config(width=20)
choice_entry.config(relief="solid")
choice_entry.config(borderwidth=5)
choice_entry.config(highlightcolor="green")
choice_entry.config(highlightthickness=10)
choice_entry.focus()
choice_entry.pack() 

login_btn = Button(root, text="Login", command=login_choice)
login_btn.config(font=("Pacifico",10))
login_btn.config(anchor=CENTER)
login_btn.config(wraplength=500)
login_btn.config(bg="white")
login_btn.config(fg="black")
login_btn.config(height=2)
login_btn.config(width=10)
login_btn.config(relief="solid")
login_btn.config(borderwidth=5)
login_btn.config(highlightcolor="green")
login_btn.config(highlightthickness=10)

login_btn.pack()

my_image = ImageTk.PhotoImage(Image.open("Images/bank.png"),master=root,height=100,width=100)
my_label = Label(image=my_image)
my_label.pack()

# Start the main GUI event loop
root.mainloop()
