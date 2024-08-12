from tkinter import *
from tkinter import Tk, Label, Entry, Button
from tkinter import messagebox
from PIL import ImageTk, Image
import  Loan, worker
import sqlite3
myDB = sqlite3.connect("MYDATABASE.db")
cursor = myDB.cursor()
window = Tk()
window.title("Bank System")
height = 650
width = 1240
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.configure(bg="#525561")



# Background Image
image_path = "bankk.png"
bg_image = Image.open(image_path)
bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
login_background_image = ImageTk.PhotoImage(bg_image)
bg_image_login = Label(window, image=login_background_image)
bg_image_login.place(x=0, y=0)

# Logo
logo_path = "bank.png"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((100, 100), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo_image)
logo_label = Label(window, image=logo, bg="#525561")
logo_label.place(x=20, y=20)

def signup():
    # Retrieve user input values from the entry fields
    username = entry_username.get()
    password = entry_password.get()
    
    if(username == "admin" and password == "0123"):
        image_path = "My project.png"
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
        login_background_image = ImageTk.PhotoImage(bg_image)
        bg_image_login = Label(window, image=login_background_image)
        bg_image_login.place(x=0, y=0)
        window.resizable(False, False)



        def add_bank():

            bank_btn = Button(window, text="Add Bank", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=add_bank)
            bank_btn.place(x=200, y=500,anchor=CENTER)

            branch_btn = Button(window, text="Add New Branch", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_branch)
            branch_btn.place(x=600, y=500,anchor=CENTER)

            employee_btn = Button(window, text="Add New Employee", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_employee)
            employee_btn.place(x=1000, y=500,anchor=CENTER)

            def submit():

                bank_btn = Button(window, text="Add Bank", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=add_bank)
                bank_btn.place(x=200, y=500,anchor=CENTER)

                branch_btn = Button(window, text="Add New Branch", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_branch)
                branch_btn.place(x=600, y=500,anchor=CENTER)

                employee_btn = Button(window, text="Add New Employee", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_employee)
                employee_btn.place(x=1000, y=500,anchor=CENTER)


                #QUERY INSERT NEW BANK #########################################################################################################################################
                code =BANKCODE.get()
                name =BANKNAME.get()
                address=BANKADDRESS.get()
                cursor.execute(f"select * from BANK where BANKNAME ='{name}'")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error", "This Bank Exist!!")
                    add_bank()  
                cursor.execute(f"select * from Bank where BANKCODE ={code}")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error","This CODE Exist!!")
                    add_bank() 
                cursor.execute(f"select * from Bank where BANKADDRESS ='{address}'")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error","This address Exist!!")
                    add_bank() 
                cursor.execute(f"insert into BANK values({code},'{name}','{address}')")
                print("operation done successfull") 
                myDB.commit()             
                ##############################################################################        
            BANKCODE = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            BANKCODE.place(x=600, y=100,anchor=CENTER)

            BANKNAME = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            BANKNAME.place(x=600, y=150,anchor=CENTER)

            BANKADDRESS = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            BANKADDRESS.place(x=600, y=200,anchor=CENTER)

            BANKCODE_label = Label(window, text="BANKCODE:", font=("Arial", 14), bg="#525561", fg="white")
            BANKCODE_label.place(x=400, y=100,anchor=CENTER)

            BANKNAME_label = Label(window,text="BANKNAME",font=("Arial", 14), bg="#525561", fg="white")
            BANKNAME_label.place(x=400, y=150,anchor=CENTER)

            BANKADDRESS_label = Label(window,text="BANKADDRESS",font=("Arial", 14), bg="#525561", fg="white")
            BANKADDRESS_label.place(x=400, y=200,anchor=CENTER)

            submit_btn = Button(window,text="Add Record To Database",command=submit,font=("Arial", 14), bg="peru", fg="white")
            submit_btn.place(x=500, y=300,anchor=CENTER)
           


        def add_branch():

            bank_btn = Button(window, text="Add Bank", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=add_bank)
            bank_btn.place(x=200, y=500,anchor=CENTER)

            branch_btn = Button(window, text="Add New Branch", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_branch)
            branch_btn.place(x=600, y=500,anchor=CENTER)

            employee_btn = Button(window, text="Add New Employee", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_employee)
            employee_btn.place(x=1000, y=500,anchor=CENTER)
            def submit():
                

                bank_btn = Button(window, text="Add Bank", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=add_bank)
                bank_btn.place(x=200, y=500,anchor=CENTER)

                branch_btn = Button(window, text="Add New Branch", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_branch)
                branch_btn.place(x=600, y=500,anchor=CENTER)

                employee_btn = Button(window, text="Add New Employee", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_employee)
                employee_btn.place(x=1000, y=500,anchor=CENTER)
            
                #QYERY NEW BRANCH ###########################################################################################################################################!
                branchNum = BRANCHNUM.get()
                branchAddress = BRANCHADDRESS.get()
                branchCode = BANKCODE.get()                
                cursor.execute(f"select * from BRANCH where BRANCHNUMBER={branchNum}")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error","This id Exist!!")
                    add_branch()  
                cursor.execute(f"select * from BRANCH where BRANCHADDRESS ='{branchAddress}'")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error","This address Exist!!")
                    add_branch()
                cursor.execute(f"select * from BANK where BANKCODE ={branchCode}")
                if(len(cursor.fetchall())!=1):
                    messagebox.showerror("Error","this bank not exist!!")
                    add_branch()
                cursor.execute(f"insert into Branch values({branchNum},{branchCode},'{branchAddress}')")
                print("operation done successfull")
                myDB.commit() 

                BRANCHNUM.delete(0, END)
                BRANCHADDRESS.delete(0,END)
                BANKCODE.delete(0,END)
                ###########################################################################################################################################!

            BRANCHNUM = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            BRANCHNUM.place(x=600, y=100,anchor=CENTER)

            BRANCHADDRESS = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            BRANCHADDRESS.place(x=600, y=150,anchor=CENTER)

            BANKCODE = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            BANKCODE.place(x=600, y=200,anchor=CENTER)

            BRANCHNUM_label = Label(window, text="BRANCHNUM:", font=("Arial", 14), bg="#525561", fg="white")
            BRANCHNUM_label.place(x=400, y=100,anchor=CENTER)

            BRANCHADDRESS_label = Label(window,text="BRANCHADDRESS",font=("Arial", 14), bg="#525561", fg="white")
            BRANCHADDRESS_label.place(x=390, y=150,anchor=CENTER)

            BANKCODE_label = Label(window,text="BANKCODE",font=("Arial", 14), bg="#525561", fg="white")
            BANKCODE_label.place(x=400, y=200,anchor=CENTER)

            submit_btn = Button(window,text="Add Record To Database",command=submit,font=("Arial", 14), bg="peru", fg="white")
            submit_btn.place(x=500, y=300,anchor=CENTER)


        def add_employee():

            bank_btn = Button(window, text="Add Bank", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=add_bank)
            bank_btn.place(x=200, y=500,anchor=CENTER)

            branch_btn = Button(window, text="Add New Branch", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_branch)
            branch_btn.place(x=600, y=500,anchor=CENTER)

            employee_btn = Button(window, text="Add New Employee", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_employee)
            employee_btn.place(x=1000, y=500,anchor=CENTER)

            def submit():
                    
                    bank_btn = Button(window, text="Add Bank", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=add_bank)
                    bank_btn.place(x=200, y=500,anchor=CENTER)

                    branch_btn = Button(window, text="Add New Branch", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_branch)
                    branch_btn.place(x=600, y=500,anchor=CENTER)

                    employee_btn = Button(window, text="Add New Employee", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_employee)
                    employee_btn.place(x=1000, y=500,anchor=CENTER)
                    #########################################################
                    WorkerId=SSN.get()
                    WorkerName=WORKERNAME.get()
                    WorkerPhone=WORKERPHONE.get()
                    WorkerAddress=WORKERADDRESS.get()
                    BranchNum=BRANCHNUM.get()
                    Positions=Position.get()
                    cursor.execute(f"select * from EMPLOYEE where EMPLOYEEID = {WorkerId} " )
                    if(len(cursor.fetchall())==1):
                        messagebox.showerror("Error", "This id Exist!!")
                        add_employee()      
                    cursor.execute(f"select * from BRANCH where BRANCHNUMBER = {BranchNum}")
                    if(len(cursor.fetchall())!=1):
                        messagebox.showerror("Error", "This id not Exist!!")
                        add_employee()   
                    cursor.execute(f"select * from EMPLOYEE where EMPLOYEENAME ='{WorkerName}'")
                    if(len(cursor.fetchall())==1):
                        messagebox.showerror("Error", "This Name Exist!!")
                        add_employee()  
                    cursor.execute(f"select * from EMPLOYEE where EMPLOYEEADDRESS ='{WorkerAddress}'")
                    if(len(cursor.fetchall())==1):
                        messagebox.showerror("Error", "This address Exist!!")
                        add_employee()
                    cursor.execute(f"select * from EMPLOYEE where EMPLOYEEPHONE ='{WorkerPhone}'")
                    if(len(cursor.fetchall())==1):
                        messagebox.showerror("Error", "This phone Exist!!")
                        add_employee()
                    cursor.execute(f"insert into EMPLOYEE values({WorkerId},{BranchNum},'{WorkerName}','{WorkerAddress}','{WorkerPhone}','{Positions}')")
                    print("operation done successfull")
                    myDB.commit()
                    #########################################################
            SSN = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            SSN.place(x=600, y=100,anchor=CENTER)

            WORKERNAME = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            WORKERNAME.place(x=600, y=150,anchor=CENTER)

            WORKERPHONE = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            WORKERPHONE.place(x=600, y=200,anchor=CENTER)

            WORKERADDRESS = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            WORKERADDRESS.place(x=600, y=250,anchor=CENTER)

            BRANCHNUM = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            BRANCHNUM.place(x=600, y=300,anchor=CENTER)

            Position = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            Position.place(x=600, y=350,anchor=CENTER)

            SSN_label = Label(window, text="SSN:", font=("Arial", 14), bg="#525561", fg="white")
            SSN_label.place(x=400, y=100,anchor=CENTER)

            WORKERNAME_label = Label(window,text="WORKERNAME",font=("Arial", 14), bg="#525561", fg="white")
            WORKERNAME_label.place(x=400, y=150,anchor=CENTER)

            WORKERPHONE_label = Label(window,text="WORKERPHONE",font=("Arial", 14), bg="#525561", fg="white")
            WORKERPHONE_label.place(x=400, y=200,anchor=CENTER)

            WORKERADDRESS_label = Label(window,text="WORKERADDRESS",font=("Arial", 14), bg="#525561", fg="white")
            WORKERADDRESS_label.place(x=400, y=250,anchor=CENTER)

            BRANCHNUM_label = Label(window,text="BRANCHNUM",font=("Arial", 14), bg="#525561", fg="white")
            BRANCHNUM_label.place(x=400, y=300,anchor=CENTER)

            Position_label = Label(window,text="Position",font=("Arial", 14), bg="#525561", fg="white")
            Position_label.place(x=400, y=350,anchor=CENTER)

            submit_btn = Button(window,text="Add Record To Database",command=submit,font=("Arial", 14), bg="peru", fg="white")
            submit_btn.place(x=500, y=400,anchor=CENTER)
        bank_btn = Button(window, text="Add Bank", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=add_bank)
        bank_btn.place(x=200, y=500,anchor=CENTER)

        branch_btn = Button(window, text="Add New Branch", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_branch)
        branch_btn.place(x=600, y=500,anchor=CENTER)

        employee_btn = Button(window, text="Add New Employee", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white",command=add_employee)
        employee_btn.place(x=1000, y=500,anchor=CENTER)

        window.mainloop()
    
    if(username == "employee" and password == "0123"):
        image_path = "My project-1.png"
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
        login_background_image = ImageTk.PhotoImage(bg_image)
        bg_image_login = Label(window, image=login_background_image)
        bg_image_login.place(x=0, y=0)
        window.resizable(False, False)
        def add_customer():
            def submit():
                    
                #####################################
                    Ssn=SSN.get()
                    CustomerName=CUSTOMERNAME.get()
                    CustomerPhone=CUSTOMERPHONE.get()
                    CustomerAddress=CUSTOMERADDRESS.get()
                    BranchNum=BRANCHNUM.get()
                    cursor.execute(f"select * from CUSTOMER where SSN ={Ssn}")
                    if(len(cursor.fetchall())==1):
                        messagebox.showerror("Error", "This id Exist!!")
                        add_customer()  
                    cursor.execute(f"select * from CUSTOMER where CUSTOMERNAME ='{CustomerName}'")
                    if(len(cursor.fetchall())==1):
                        messagebox.showerror("Error", "This Name Exist!!")
                        add_customer()  
                    cursor.execute(f"select * from CUSTOMER where CUSTOMERADDRESS ='{CustomerAddress}'")
                    
                    cursor.execute(f"select * from CUSTOMER where CUSTOMERPHONE ='{CustomerPhone}'")
                    if(len(cursor.fetchall())==1):
                        messagebox.showerror("Error", "This phone Exist!!")
                        add_customer()
                    cursor.execute(f"select * from BRANCH where BRANCHNUMBER ={BranchNum}")
                    if(len(cursor.fetchall())!=1):
                        messagebox.showerror("Error", "This Branch not Exist!!")
                        add_customer()
                    cursor.execute(f"insert into CUSTOMER values({Ssn},{BranchNum},'{CustomerName}','{CustomerPhone}','{CustomerAddress}')")
                    print("operation done successfull")
                    myDB.commit()
                    ###########################################################3


            
            def List_Customer():
                list_customer_query = Tk()
                list_customer_query.title("List Customer")
                list_customer_query.geometry("500x500")
                list_customer_query.configure(bg="#525561")
                
                cursor.execute("select * from customer")
                result = cursor.fetchall()# list

                for index , x in enumerate(result):
                 num = 0
                 for y in x:
                   LookupLable = Label(list_customer_query, text = y )
                   LookupLable.grid(row = index , column=num)
                   num+=1

                    
    
            SSN = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            SSN.place(x=600, y=300,anchor=CENTER)

            CUSTOMERNAME = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            CUSTOMERNAME.place(x=600, y=340,anchor=CENTER)

            CUSTOMERPHONE = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            CUSTOMERPHONE.place(x=600, y=380,anchor=CENTER)

            CUSTOMERADDRESS = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            CUSTOMERADDRESS.place(x=600, y=420,anchor=CENTER)

            BRANCHNUM = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            BRANCHNUM.place(x=600, y=460,anchor=CENTER)

            SSN_label = Label(window, text="SSN:", font=("Arial", 14), bg="#525561", fg="white")
            SSN_label.place(x=450, y=300,anchor=CENTER)

            CUSTOMERNAME_label = Label(window,text="CUSTOMERNAME",font=("Arial", 14), bg="#525561", fg="white")
            CUSTOMERNAME_label.place(x=400, y=340,anchor=CENTER)

            CUSTOMERPHONE_label = Label(window,text="CUSTOMERPHONE",font=("Arial", 14), bg="#525561", fg="white")
            CUSTOMERPHONE_label.place(x=390, y=380,anchor=CENTER)

            CUSTOMERADDRESS_label = Label(window,text="CUSTOMERADDRESS",font=("Arial", 14), bg="#525561", fg="white")
            CUSTOMERADDRESS_label.place(x=380, y=420,anchor=CENTER)

            BRANCHNUM_label = Label(window,text="BRANCHNUM",font=("Arial", 14), bg="#525561", fg="white")
            BRANCHNUM_label.place(x=390, y=460,anchor=CENTER)

            submit_btn = Button(window,text="Add Record To Database",command=submit,font=("Arial", 14), bg="peru", fg="white")
            submit_btn.place(x=600, y=500,anchor=CENTER)

            list_Customer_button=Button(window,text="List Customer",command=List_Customer,font=("Arial", 14), bg="peru", fg="white")
            list_Customer_button.place(x=600, y=550,anchor=CENTER)

        # Add new customer logic here

        customer_btn = Button(window, text="Add New Customer",activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white" ,command=add_customer)
        customer_btn.place(x=610, y=200,anchor=CENTER)

        window.mainloop()

    if(username == "customer" and password == "0123"):
        image_path = "My project (1).png"
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
        login_background_image = ImageTk.PhotoImage(bg_image)
        bg_image_login = Label(window, image=login_background_image)
        bg_image_login.place(x=0, y=0)
        window.resizable(False, False)

        def Show_balance():
            image_path = "My project (1).png"
            bg_image = Image.open(image_path)
            bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
            login_background_image = ImageTk.PhotoImage(bg_image)
            bg_image_login = Label(window, image=login_background_image)
            bg_image_login.place(x=0, y=0)
            window.resizable(False, False)

            update_btn = Button(window, text="Updata data", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=Updata_data)
            update_btn.place(x=200, y=500,anchor=CENTER)

            balance_btn = Button(window, text="Show balance", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=Show_balance)
            balance_btn.place(x=600, y=500,anchor=CENTER)

            loan_btn = Button(window, text="request loan", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=request_loan)
            loan_btn.place(x=1000, y=500,anchor=CENTER)


            def submit():
                account_num = ACCOUNTNUM.get()
                account_type = ACCOUNTTYPE.get()
                balance = BALANCE.get()
                ssn = SSN.get()
                cursor.execute(f"select * from ACCOUNT where ACCOUNTNUM = {account_num}")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error", "This id Exist!!")
                    Show_balance()
                cursor.execute(f"select * from ACCOUNT where ACCOUNTTYPE ='{account_type}'")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error", "This type Exist!!")
                    Show_balance()
                cursor.execute(f"select * from ACCOUNT where BALANCE ='{balance}'")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error", "This balance Exist!!")
                    Show_balance()
                cursor.execute(f"select * from ACCOUNT where SSN ='{ssn}'")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error", "This ssn Exist!!")
                    Show_balance()
                cursor.execute(f"insert into ACCOUNT values({account_num},'{account_type}',{balance},{ssn})")
                print("operation done successfull")
                myDB.commit()
                ###########################################################################################################################################!
                

                
            
            ACCOUNTNUM = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            ACCOUNTNUM.place(x=600, y=100,anchor=CENTER)

            ACCOUNTTYPE = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            ACCOUNTTYPE.place(x=600, y=150,anchor=CENTER)

            BALANCE = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            BALANCE.place(x=600, y=200,anchor=CENTER)

            SSN = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            SSN.place(x=600, y=250,anchor=CENTER)

            ACCOUNTNUM_label = Label(window, text="ACCOUNTNUM:", font=("Arial", 14), bg="#525561", fg="white")
            ACCOUNTNUM_label.place(x=400, y=100,anchor=CENTER)

            ACCOUNTTYPE_label = Label(window,text="ACCOUNTTYPE",font=("Arial", 14), bg="#525561", fg="white")
            ACCOUNTTYPE_label.place(x=400, y=150,anchor=CENTER)

            BALANCE_label = Label(window,text="BALANCE",font=("Arial", 14), bg="#525561", fg="white")
            BALANCE_label.place(x=400, y=200,anchor=CENTER)

            SSN_label = Label(window,text="SSN",font=("Arial", 14), bg="#525561", fg="white")
            SSN_label.place(x=400, y=250,anchor=CENTER)

            submit_btn = Button(window,text="Add Record To Database",command=submit,font=("Arial", 14), bg="peru", fg="white")
            submit_btn.place(x=500, y=300,anchor=CENTER)
            

        def request_loan():
            image_path = "My project (1).png"
            bg_image = Image.open(image_path)
            bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
            login_background_image = ImageTk.PhotoImage(bg_image)
            bg_image_login = Label(window, image=login_background_image)
            bg_image_login.place(x=0, y=0)
            window.resizable(False, False)

            update_btn = Button(window, text="Updata data", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=Updata_data)
            update_btn.place(x=200, y=500,anchor=CENTER)

            balance_btn = Button(window, text="Show balance", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=Show_balance)
            balance_btn.place(x=600, y=500,anchor=CENTER)

            loan_btn = Button(window, text="request loan", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=request_loan)
            loan_btn.place(x=1000, y=500,anchor=CENTER)



            def submit():


                #####################################
                LoneNum=LOANNUM.get()
                BranchNum=BRANCHNUM.get()
                LoanType=LOANTYPE.get()
                Amount=AMOUNT.get()
                SSN=SSN.get()
                EmployeeId=EMPLOYEEID.get()
                cursor.execute(f"select * from LOAN where LOANNUM = {LoneNum}")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error", "This id Exist!!")
                    request_loan()
                cursor.execute(f"select * from BRANCH where BRANCHNUMBER = {BranchNum}")
                if(len(cursor.fetchall())!=1):
                    messagebox.showerror("Error", "This bank not Exist!!")
                    request_loan()
                cursor.execute(f"select * from LOAN where LOANTYPE ='{LoanType}'")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error", "This type Exist!!")
                    request_loan()
                cursor.execute(f"select * from LOAN where AMOUNT ={Amount}")
                if(len(cursor.fetchall())==1):
                    messagebox.showerror("Error", "This amount Exist!!")
                    request_loan()
                cursor.execute(f"select * from EMPLOYEE where EMPLOYEEID ={EmployeeId}")
                if(len(cursor.fetchall())!=1):
                    messagebox.showerror("Error", "This employee not Exist!!")
                    request_loan()
                stat = "Pending"
                cursor.execute(f"insert into LAONS values({LoneNum},{BranchNum},'{LoanType}',{Amount},'{stat}')")
                cursor.execute(f"insert into take values({SSN},{LoneNum})")
                print("operation done successfull")
                myDB.commit()
                ###########################################################################################################################################!
                

            
            def List_loan():
                list_customer_query = Tk()
                list_customer_query.title("List loan")
                list_customer_query.geometry("500x500")
                list_customer_query.configure(bg="#525561")
                
                cursor.execute("""
                                                SELECT CUSTOMER.CUSTOMERNAME, EMPLOYEE.EMPLOYEENAME,LAONS.LOANNUMBER,LAONS.STATUS,LAONS.LOANNUMBER,LAONS.BRANCHNUMBER,LAONS.LAONTYPE,LAONS.LOANAMOUNT
                                                FROM LAONS
                                                INNER JOIN TAKE ON LAONS.LOANNUMBER = TAKE.LOANNUMBER
                                                INNER JOIN CUSTOMER ON TAKE.SSN = CUSTOMER.SSN
                                                INNER JOIN MANGE ON LAONS.LOANNUMBER = MANGE.LOANNUMBER
                                                INNER JOIN EMPLOYEE ON MANGE.EMPLOYEEID = EMPLOYEE.EMPLOYEEID;
                                       """)
                result = cursor.fetchall()
                for index , x in enumerate(result):
                    num = 0
                    for y in x:
                         LookupLable = Label(list_customer_query, text = y )
                         LookupLable.grid(row = index , column=num)
                         num+=1
                         
            LOANNUM = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            LOANNUM.place(x=600, y=100,anchor=CENTER)

            BRANCHNUM = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            BRANCHNUM.place(x=600, y=150,anchor=CENTER)

            clicked=StringVar()
            clicked.set("industry loan")

            LOANTYPE = OptionMenu(window, clicked, "industry loan", "commercial loan", "Personal loan")
            LOANTYPE.place(x=600, y=200,anchor=CENTER)

            AMOUNT = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            AMOUNT.place(x=600, y=250,anchor=CENTER)

            SSN = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            SSN.place(x=600, y=300,anchor=CENTER)

            EMPLOYEEID = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            EMPLOYEEID.place(x=600, y=350,anchor=CENTER)

            LOANNUM_label = Label(window, text="LOANNUM:", font=("Arial", 14), bg="#525561", fg="white")
            LOANNUM_label.place(x=400, y=100,anchor=CENTER)

            BRANCHNUM_label = Label(window,text="BRANCHNUM",font=("Arial", 14), bg="#525561", fg="white")
            BRANCHNUM_label.place(x=400, y=150,anchor=CENTER)

            LOANTYPE_label = Label(window,text="LOANTYPE",font=("Arial", 14), bg="#525561", fg="white")
            LOANTYPE_label.place(x=400, y=200,anchor=CENTER)

            AMOUNT_label = Label(window,text="AMOUNT",font=("Arial", 14), bg="#525561", fg="white")
            AMOUNT_label.place(x=400, y=250,anchor=CENTER)

            SSN_label = Label(window,text="SSN",font=("Arial", 14), bg="#525561", fg="white")
            SSN_label.place(x=400, y=300,anchor=CENTER)

            EMPLOYEEID_label = Label(window,text="EMPLOYEEID",font=("Arial", 14), bg="#525561", fg="white")
            EMPLOYEEID_label.place(x=400, y=350,anchor=CENTER)

            submit_btn = Button(window,text="Add Record To Database",command=submit,font=("Arial", 14), bg="peru", fg="white")
            submit_btn.place(x=500, y=400,anchor=CENTER)
            list_Customer_button=Button(window,text="List loan",command=List_loan,font=("Arial", 14), bg="peru", fg="white")
            list_Customer_button.place(x=600, y=550,anchor=CENTER)

        def Updata_data():
            image_path = "My project (1).png"
            bg_image = Image.open(image_path)
            bg_image = bg_image.resize((width, height), Image.ANTIALIAS)
            login_background_image = ImageTk.PhotoImage(bg_image)
            bg_image_login = Label(window, image=login_background_image)
            bg_image_login.place(x=0, y=0)
            window.resizable(False, False)

            update_btn = Button(window, text="Updata data", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=Updata_data)
            update_btn.place(x=200, y=500,anchor=CENTER)

            balance_btn = Button(window, text="Show balance", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=Show_balance)
            balance_btn.place(x=600, y=500,anchor=CENTER)

            loan_btn = Button(window, text="request loan", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=request_loan)
            loan_btn.place(x=1000, y=500,anchor=CENTER)
            
            def submit():


                #####################################
                Ssn=SSN.get()
                CustomerName=CUSTOMERNAME.get()
                CustomerPhone=CUSTOMERPHONE.get()
                CustomerAddress=CUSTOMERADDRESS.get()
                BranchNum=BRANCHNUM.get()
                id = Ssn
                cursor.execute(f"select * from CUSTOMER where SSN = {id}")
                if(len(cursor.fetchall())!=1):
                    messagebox.showerror("Error", "This id not Exist!!")
                    Updata_data()
                BranchNumber = BranchNum
                cursor.execute(f"select * from BRANCH where BRANCHNUMBER = {BranchNumber}")
                if(len(cursor.fetchall())!=1):
                    messagebox.showerror("Error", "This id not Exist!!")
                    Updata_data()
                name = CustomerName
                cursor.execute(f"select * from CUSTOMER where CUSTOMERNAME ='{name}'")  
                if(len(cursor.fetchall())!=1):
                    messagebox.showerror("Error", "This Name not Exist!!")
                    Updata_data()
                address = CustomerAddress
                cursor.execute(f"select * from CUSTOMER where CUSTOMERADDRESS ='{address}'")
                if(len(cursor.fetchall())!=1):
                    messagebox.showerror("Error", "This address not Exist!!")
                    Updata_data()
                phone = CustomerPhone
                cursor.execute(f"select * from CUSTOMER where CUSTOMERPHONE ='{phone}'")
                if(len(cursor.fetchall())!=1):
                    messagebox.showerror("Error", "This phone not Exist!!")
                    Updata_data()
                cursor.execute(f"update CUSTOMER set CUSTOMERNAME = '{name}' , CUSTOMERPHONE = '{phone}' , CUSTOMERADDRESS = '{address}' , BRANCHNUM = {BranchNumber} where SSN = {id}")
                print("operation done successfull")
                myDB.commit()
                ###########################################################################################################################################!


                
                    

            SSN = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            SSN.place(x=600, y=100,anchor=CENTER)

            CUSTOMERNAME = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            CUSTOMERNAME.place(x=600, y=150,anchor=CENTER)

            CUSTOMERPHONE = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            CUSTOMERPHONE.place(x=600, y=200,anchor=CENTER)

            CUSTOMERADDRESS = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            CUSTOMERADDRESS.place(x=600, y=250,anchor=CENTER)

            BRANCHNUM = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
            BRANCHNUM.place(x=600, y=300,anchor=CENTER)

            SSN_label = Label(window, text="SSN:", font=("Arial", 14), bg="#525561", fg="white")
            SSN_label.place(x=450, y=100,anchor=CENTER)

            CUSTOMERNAME_label = Label(window,text="CUSTOMERNAME",font=("Arial", 14), bg="#525561", fg="white")
            CUSTOMERNAME_label.place(x=370, y=150,anchor=CENTER)

            CUSTOMERPHONE_label = Label(window,text="CUSTOMERPHONE",font=("Arial", 14), bg="#525561", fg="white")
            CUSTOMERPHONE_label.place(x=370, y=200,anchor=CENTER)

            CUSTOMERADDRESS_label = Label(window,text="CUSTOMERADDRESS",font=("Arial", 14), bg="#525561", fg="white")
            CUSTOMERADDRESS_label.place(x=370, y=250,anchor=CENTER)

            BRANCHNUM_label = Label(window,text="BRANCHNUM",font=("Arial", 14), bg="#525561", fg="white")
            BRANCHNUM_label.place(x=370, y=300,anchor=CENTER)

            submit_btn = Button(window,text="Add Record To Database",command=submit,font=("Arial", 14), bg="peru", fg="white",)
            submit_btn.place(x=600, y=400,anchor=CENTER)
            
        update_btn = Button(window, text="Updata data", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=Updata_data)
        update_btn.place(x=200, y=500,anchor=CENTER)

        balance_btn = Button(window, text="Show balance", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=Show_balance)
        balance_btn.place(x=600, y=500,anchor=CENTER)

        loan_btn = Button(window, text="request loan", activebackground="dim gray",font=("Arial", 20), bg="Silver", fg="white", command=request_loan)
        loan_btn.place(x=1000, y=500,anchor=CENTER)

        window.mainloop()

    else:
        messagebox.showerror("Error", "Wrong username or password")




title_label1 = Label(window, text="Bank System", font=("Arial", 40, "bold"), bg="#525561", fg="white")
title_label1.place(relx=0.5, rely=0.15, anchor=CENTER)

title_label2 = Label(window, text="Signup Form", font=("Arial", 40, "bold"), bg="#525561", fg="white")
title_label2.place(relx=0.5, rely=0.35, anchor=CENTER)

# Signup Form
label_username = Label(window, text="Username:", font=("Arial", 14), bg="#525561", fg="white")
label_username.place(x=450, y=400,anchor=CENTER)
entry_username = Entry(window, font=("Arial", 14), bg="#D3D3D3", fg="black")
entry_username.place(x=650, y=400,anchor=CENTER)

label_password = Label(window, text="Password:", font=("Arial", 14), bg="#525561", fg="white")
label_password.place(x=450, y=450,anchor=CENTER)
entry_password = Entry(window, show="*", font=("Arial", 14), bg="#D3D3D3", fg="black")
entry_password.place(x=650, y=450,anchor=CENTER)

button_signup = Button(window, text="Sign Up", font=("Arial", 14), bg="#4B8BBE", fg="white", command=signup)
button_signup.place(x=620, y=500,anchor=CENTER)


window.resizable(False, False)
window.mainloop()