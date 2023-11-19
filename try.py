from ast import While
from distutils.util import execute
from sys import meta_path
import pymysql                # import pymysql library 
try:
    conn=pymysql.connect(host='localhost',user='root',password='',db='bank') # connection for DataBase
except Exception as e:
    print(e)
else:
    print('connection succesfully created')  

class OpenNewAcc(): # Open New Account Class  # Base class
    def gets(self):
        while True:     # Exception Handling for invalid input
            try:
                self.__accountno=int(input("Enter Account No:"))
            except Exception as no:
                print("Plz Enter Numerical Value.")
            else:
                break

        self.__accountname=input("Enter Account Holder Name:")
            
        while True:
            try:
                self.__age=int(input("Enter Your Age:"))
            except Exception as age:
                print("Plz Enter Numerical Value.")
            else:
                break
        while True:
            try:
                self._balance=float(input("Enter Amount To Deposit:"))
            except Exception as bal:
                print("Plz Enter Numerical Value.")
            else: 
                break
        data=(self.__accountno,self.__accountname,self.__age,self._balance)
        query="insert into account(account_no,name,age,balance)values(%s,%s,%s,%s)"
        cur=conn.cursor()
        try:
            cur.execute(query,data)
        except Exception as e1:
            print("Query Error")
        else:
            conn.commit()
            print('Data Entered Successfully')                     
                    
                        
o=OpenNewAcc()  # Object for open new account class

class BalanceEnquiry(OpenNewAcc): # Balance enquiry class  # derived class
    def gets(self):
        self.__accountno=int(input("Enter Account No:"))
        d=(self.__accountno)
        query='select balance from account where account_no=%s'  # Query for mysql
        cur=conn.cursor()
        try:
            cur.execute(query,d)
        except Exception as bal:
            print(bal)
        else:
            f=cur.fetchall()
            print("Balance:",f)     
be=BalanceEnquiry()  # Object for balance enquiry class

    
class Deposite(OpenNewAcc): # Add money to account  # derived class
    def gets(self):
        self.__accountno=int(input("Enter account no:"))
        self.__amt=int(input("Enter Amount:"))
        #d=(self.__accountno) 
        query='select balance from account where account_no=%s'  # selecting balance from given account no
        cur=conn.cursor()
        try:
            cur.execute(query,self.__accountno)  

        except Exception as dep:
            print(dep)
        else:
            
            f=cur.fetchall()      # fetcah all record from given account no  
            if f:
                for row in f:
                    t=row[0]+self.__amt        # adding given amount in Balance
                    print("New Balance:",t)
            else:
                pass
        
        d=(t,self.__accountno)
        query='update account set balance=%s where account_no=%s'  # update balace query
        try:
            cur.execute(query,d)
            conn.commit()
        except Exception as e:
            print(e)
        print("data update")
    
de=Deposite()  # object for Deposit Money in account

       
class withDrawal(OpenNewAcc): # Removing money from account
    def gets(self):
        self.__accountno=int(input("Enter Account No:"))
        self.__amt=float(input("Withdrawl Amount:"))
        query='select balance from account where account_no=%s' # query from selecting balance from given account no
        cur=conn.cursor()
        try:
            cur.execute(query,self.__accountno)
        except Exception as dep:
            print(dep)
        else:  
            f=cur.fetchall()    # fetcah all record from given account no 
            if f:
                for row in f:
                    t=row[0]-self.__amt
                    print("New Balance:",t)  # print new balance 
            else:
                pass
    
        d=(t,self.__accountno)
        query='update account set balance=%s where account_no=%s'   # update balace query
        try:
            cur.execute(query,d)
            conn.commit()
        except Exception as e:
            print(e)
        print("data update")
        
wd=withDrawal() # object for withdrawal moeney

class ShowDetails(OpenNewAcc): # derived class 
    def gets(self):
        self.__accountno=int(input("Enter Account No:"))
        d=(self.__accountno)
        query='select * from account where account_no=%s' # query from selecting all details from given account no
        cur=conn.cursor()
        try:
            cur.execute(query,d)
        except Exception as show:
            print(show)
        else:
            f=cur.fetchall()
            print("----Account Details----")
            for i in f:
                print("Account No:",i[0])   # print all details one by one
                print("Name:",i[1])
                print("Age:",i[2])
                print("Balance:",i[3])
                print("Loan:",i[4])
sd=ShowDetails() # object for showdetails


class Loan(OpenNewAcc):
    def apply(self):
        self.__accountno=int(input("Enter your Account No:"))
        query='SELECT EXISTS(SELECT account_no from account WHERE account_no=%s)' # query for cheching if account holder or not
        cur=conn.cursor()
        try:
            cur.execute(query,self.__accountno)
        except Exception as loan:
            print(loan)
        else:  
            f=cur.fetchall()

            if f :
                self.__salary=float(input("Enter Your Salary:")) # checking if user is account holder
                if self.__salary>=25000:        # accept if is more than 25,000
                    print("You Are Eligible.")
                    print('''Enter 1:To Apply for Loan.           # menu for loan porpose
                             Enter 2:To Clear Your loan''')
                    ch1=int(input("Select Your Choice."))
    
                    if ch1==1:           # if want to apply for loan
                        self.__loan=int(input("Enter Amount For Loan:"))
                        self.__accountno=int(input("Enter Account No:"))
                        data=(self.__loan,self.__accountno)
                        query='update account set loan=%s where account_no=%s' # query to insert loan amount in data base
                        cur=conn.cursor()
                        try:
                            cur.execute(query,data)
                        except Exception as e1:
                            print("Query Error")
                        else:
                            conn.commit()
                            print('Loan Amount Deposit.') 
                    elif ch1==2:   # if want for clear loan
                        self.__accountno=int(input("Enter Account No:"))
                        self.__null='Null'
                        data=(self.__null,self.__accountno)
                        query='update account set loan=%s where account_no=%s'  #query to insert null amount in data base
                        cur=conn.cursor()
                        try:
                            cur.execute(query,data)
                        except Exception as e1:
                            print("Query Error")
                        else:   # if pressed nay time excpt 1 and 2 will break loop
                            conn.commit()
                            print('You have clear Your Loan.') 
                    else:
                        pass
                else:
                    print("Unfortunately, Your are not eligible for loan as your salary does'nt meet our criteria.")
            else:
                print("Oops! You don't have an account in our Bank. Apply.")          
        
l=Loan()  # object for laon class

class CloseAccount(ShowDetails): #derived class 
    def gets(self):
        self.__accountno=int(input("Enter Account No:"))
        d=(self.__accountno)
        query='delete from account where account_no=%s' # query to delete account 
        cur=conn.cursor()
        try:
            cur.execute(query,d)
            f=cur.fetchall()
        except Exception as show:
            print(show)
        else:
            print("Account Deleted",f)
c=CloseAccount()


# MAIN PROGRAM
while True:
    print("********************************")
    print("***Bank Management System*******")
    print("********************************")
                                              # menu for Bank system 
    print('''                           
    Enter 1:To Open New Account           
    Enter 2:To Deposit Money
    Enter 3:To Withdraw Money
    Enter 4:To Balance Enquiry
    Enter 5:To Show Account Detail
    Enter 6:To Loan Option
    Enter 7:TO Close Your Account
    Enter 8:To Exit
    ''')
    while True:    
        try:
            ch=int(input("Select Your Option(1-8):"))
        except Exception as mp:
            print(mp)
        else:
            break
    
    if ch==1:
        o.gets()   # calling open new account class
    elif ch==2:
        de.gets()  # calling deposit class
    elif ch==3:
        wd.gets()  # calling withdrawal class
    elif ch==4:
         be.gets()  # calling balance enquiry class
    elif ch==5:
        sd.gets()   # calling show details class
    elif ch==6:
        l.apply()  # calling loan classs
    elif  ch==7:
        c.gets()  # close your account class
    else:
        break   # leave the loop





