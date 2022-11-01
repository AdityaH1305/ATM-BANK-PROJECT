import tkinter as tk
from tkinter import messagebox
import mysql.connector as mycon
from PIL import Image
con=mycon.connect(host='localhost',user='root',password='12345',database='ATM_MACHINE')
c1=con.cursor()
print('========================================================================')

print('WELCOME TO THE AVN BANK')

print('========================================================================')

while True:
    print('1. ADMIN LOGIN')
    print('2. CUSTOMER ATM LOGIN')
    print('3. EXIT')

    ch=int(input("SELECT YOUR ACTION::"))

    if ch==1:
        import tkinter as tk
        import mysql.connector
        from tkinter import *
        from PIL import Image
        def Login():
            
            user = Username.get()
            if user=='ADIS':
                passw = password.get()
                if passw=='12C':
                    messagebox.showinfo('Welcome','Login Successful')
                else:
                    messagebox.showinfo('Oops','Wrong Password')
            else:
                messagebox.showinfo('Error','Wrong Username')
        
            print(f"The name entered by you is {user} {passw}")
        
            logintodb(user, passw)
        
        
        def logintodb(user, passw):
            
            # If password is enetered by the
            # user
            if passw:
                db = mysql.connector.connect(host ="localhost",user='root',password='12345',db ="ATM_MACHINE")
                cursor = db.cursor()
                
            # If no password is enetered by the
            # user
            else:
                db = mysql.connector.connect(host ="localhost",user='root',password='12345',db ="ATM_MACHINE")
                cursor = db.cursor()
                
            # A Table in the database
            savequery = "select * from RECORDS"
            
            try:
                cursor.execute(savequery)
                myresult = cursor.fetchall()
                
                # Printing the result of the
                # query
                for x in myresult:
                    print(x)
                print("SUCCESSFUL")
                
            except:
                db.rollback()
                print("Error occured")
            
            root.destroy()
        
        
        
        root = tk.Tk()
        root.geometry("800x700")
        root.title("AVN ADMIN")
        bg = PhotoImage(file = "C://Users//DELL//Downloads//atm_img.png")
        root.iconbitmap("C://Users//DELL//Downloads//atm_icon.ico")

        label1= Label(root, image=bg)
        label1.place(x=0, y=0)
        
        
        # Defining the first row
        lblfrstrow = tk.Label(root, text ="Username -", )
        lblfrstrow.place(x = 275, y = 350)
        
        Username = tk.Entry(root, width = 55)
        Username.place(x = 350, y = 350, width = 75)
        
        lblsecrow = tk.Label(root, text ="Password -")
        lblsecrow.place(x = 275, y = 400)

        password = tk.Entry(root, width = 100, show='*')
        password.place(x = 350, y = 400, width = 75)
        
        submitbtn = tk.Button(root, text ="Login",
                            bg ='yellow', command = Login)
        submitbtn.place(x = 300, y = 435, width = 55)

        root.mainloop()
           

        import mysql.connector as mycon
        con=mycon.connect(host='localhost',user='root',password='12345',database='ATM_MACHINE')
        c1=con.cursor()

        print('WELCOME ADMIN')
        print('========================================================================')

        while True:
            print('1.Create a new account!')
            print('2.Show the data of all customers')
            print('3.Update the name of the customers')
            print('4.Delete all data')
            print('5.Create the database table')
            print('6.Exit')
            
            ch=int(input("Enter your choice 1/2/3/4/5/6-"))
            if ch==1:
                m='n'
                while m=='n':
                    acct_no=int(input("Enter 4 digits for your account number:-"))
                    a=("Select * from RECORDS where ACCOUNT_NO={}".format(acct_no))
                    c1.execute(a)
                    b=c1.fetchall()
                    data=c1.rowcount
                    
                    if data==1:
                        print("========================================================================")
                        
                        print("THIS ACCOUNT NUMBER IS ALREADY TAKEN")
                        
                        print('========================================================================')
                    
                            
                    else:
                        Name=input("Enter your name:")
                        pin=int(input("Enter your pin code:"))
                        ins=("insert into RECORDS(ACCOUNT_NO,PINCODE,NAME) values({},{},'{}')").format(acct_no,pin,Name)
                        print('========================================================================')
                        
                        c1.execute(ins)
                        con.commit()
                        print('Your account has been successfully created')
                        print('WELCOME',Name)
                        print('========================================================================')
                        
                        s=int(input("Enter the amount of money to be deposited:"))
                        print('========================================================================')
                        
                        up=('update RECORDS set CR_AMOUNT={} where ACCOUNT_NO={}').format(s,acct_no)
                        c1.execute(up)
                        con.commit()
                        up1=("update RECORDS set balance=CR_AMOUNT where ACCOUNT_NO={}").format(acct_no)
                        c1.execute(up1)
                        con.commit()
                        print('The requested amount has been successfully deposited')
                        
                        print('THANK YOU VERY MUCH')
                        break

            if ch==2:
                quer=('SELECT * from RECORDS')
                c1.execute(quer)
                print('%10s %10s %10s %10s %10s %10s' % ('ACCNO','Password','Name','CR_AMT','WITHDRAWAL','BALANCE'))
                for i in c1:
                    print('%10s %10s %10s %10s %10s %10s' % (i[0],i[1],i[2],i[3],i[4],i[5]))
                
                

            if ch==3:
                acc=int(input("Enter your account number:"))
                sel=("Select * from RECORDS where ACCOUNT_NO={}").format(acc)
                c1.execute(sel)
                c1.fetchall()
                da=c1.rowcount
                if da==1:
                    p=int(input("Enter your pincode:-"))
                    print('========================================================================')
                    sel1=("Select pincode from RECORDS where ACCOUNT_NO={}").format(acc)
                    c1.execute(sel1)
                    a=c1.fetchone()
                    a1=list(a)
                    i=input("Enter your name:")
                    cb="select * from records where ACCOUNT_NO={}".format(acc)
                    c1.execute(cb)
                    c1.fetchall()
                    data=c1.rowcount
                    ar=("UPDATE RECORDS set NAME='{}' where ACCOUNT_NO={}").format(i,acc)
                    c1.execute(ar)
                    con.commit()
                    print("Your new name is ",i)

                else:
                    print('Wrong Account Number or Wrong Pincode')
                        
            if ch==4:
                del1=('DROP TABLE RECORDS')
                c1.execute(del1)
                con.commit()
            
            if ch==5:
                import mysql.connector as mycon
                con=mycon.connect(host='localhost',user='root',password='12345',database='ATM_MACHINE')
                if con.is_connected():
                    print("Sucessfully Connected")
                c1=con.cursor()
                db="CREATE TABLE RECORDS( ACCOUNT_NO  INT(4) primary key,PINCODE INT(3),NAME VARCHAR(20),CR_AMOUNT INT (6),WITHDRAWAL INT (6) default 0 ,BALANCE INT (6))"
                c1.execute(db)
                print("Sucessfully Created")
            if ch==6:
                print('Successfully exited')
                break

    if ch==2:
        print('1.Login to your account!')
        print('2.Exit the ATM')
        print('========================================================================')

        ch=int(input('Select your action!:-'))
        print('========================================================================')

        

        if ch==1:
            a='b'
            while a=='b':
                
                acc=int(input("Enter your account number:"))
                sel=("Select * from RECORDS where ACCOUNT_NO={}").format(acc)
                c1.execute(sel)
                c1.fetchall()
                da=c1.rowcount
                
                if da==1:
                    p=int(input("Enter your pincode:-"))
                    print('========================================================================')
                    
                    sel1=("Select pincode from RECORDS where ACCOUNT_NO={}").format(acc)
                    c1.execute(sel1)
                    a=c1.fetchone()
                    a1=list(a)
                    
                    while True:
                        if p==a1[0]:
                            print('WELCOME')
                            print("1.Deposit")
                            print("2.Withdraw")
                            print("3.Transfer")
                            print("4.Check Balance")
                            print("5.Change Pincode")
                            print("6.Log Out")
                
                                                
                            print('========================================================================')
                            
                            i=int(input("Enter your choice:"))
                            print('========================================================================')
                            
                            if i==1:
                                amt=int(input("Enter the amount of money to be deposited:"))
                                print('========================================================================')
                                
                                up2=("update RECORDS set CR_AMOUNT=CR_AMOUNT+{} where ACCOUNT_NO={}").format(amt,acc)
                                c1.execute(up2)
                                con.commit()
                                up3=("update RECORDS set balance=CR_AMOUNT-WITHDRAWAL where ACCOUNT_NO={}").format(acc)
                                c1.execute(up3)
                                con.commit()
                                print("THE REQUESTED AMOUNT HAS BEEN SUCCESSFULLY DEPOSITED")

                                y=input("Do You Want To Continue?:")
                                if y=='Yes' or y=='yes':
                                    continue
                                else:
                                    print('Thank you')
                                    break
                                
                            
                                    
                            if i==2:
                                amt=int(input("Enter the amount of money to be withdrawn:"))
                                print('========================================================================')
                                
                                lol=("Select BALANCE from RECORDS where ACCOUNT_NO={}").format(acc)
                                c1.execute(lol)
                                f=c1.fetchone()
                                
                                if amt>f[0]:
                                    print('Your balance is short')
                                    print('Please try again later')
                                    print('========================================================================')
                                
                                else:
                                    b=("update RECORDS set BALANCE=BALANCE-{} where ACCOUNT_NO={}").format(amt,acc)
                                    c=("update RECORDS set WITHDRAWAL={} where ACCOUNT_NO={}").format(amt,acc)
                                    c1.execute(c)
                                    c1.execute(b)
                                    con.commit()
                                    print('The requested amount has been successfully withdrawn')
                                    y=input("Do You Want To Continue?:")
                                    if y=='Yes' or y=='yes':
                                        continue
                                    else:
                                        print('Thank You')
                                        break
                                
                            
                                    
                            if i==3:
                                tran=int(input("Enter the account number to be transferred to:"))
                                print('========================================================================')
                                
                                h=("select * from RECORDS where ACCOUNT_NO={}").format(tran)
                                c1.execute(h)
                                c1.fetchall()
                                data=c1.rowcount
                                
                                if data==1:
                                    print(tran,'Number Exists')
                                    l=int(input("Enter the amount of money to be transferred:"))
                                    print('========================================================================')
                                    
                                    k=("select BALANCE from RECORDS where ACCOUNT_NO={}").format(acc)
                                    c1.execute(k)
                                    p=c1.fetchone()
                                    if l>p[0]:
                                        print('Your balance is less than',l)
                                        print('Please try again later')
                                        print('========================================================================')
                                        
                                    else:
                                        n=('update RECORDS set BALANCE=BALANCE-{} where ACCOUNT_NO={}').format(l,acc)
                                        v=('update RECORDS set BALANCE=BALANCE+{} where ACCOUNT_NO={}').format(l,tran)
                                        w=('update RECORDS set WITHDRAWAL=WITHDRAWAL+{} where ACCOUNT_NO={}').format(l,acc)
                                        u=('update RECORDS set CR_AMOUNT=CR_AMOUNT+{} where ACCOUNT_NO={}').format(l,tran)
                                        c1.execute(n)
                                        c1.execute(v)
                                        c1.execute(w)
                                        c1.execute(u)
                                        con.commit()
                                        print('SUCCESSFUL')
                                y=input("Do You Want To Continue?:")
                                if y=='Yes' or y=='yes':
                                    continue
                                else:
                                    print('Thank You')
                                    break
                                    
                                    
                            
                        if i==4:
                            b=('select  BALANCE from RECORDS where ACCOUNT_NO={}').format(acc)
                            c1.execute(b)
                            print('%10s' %('BALANCE'))
                            for i in c1:
                                print('%10s' % (i[0]))
                            print('========================================================================')
                            
                            y=input('Do you want to continue yes/no?')
                            if y=='Yes' or y=='yes':
                                continue
                            else:
                                print('Thank You Very Much')
                                break
                        
                            
                        if i==5:
                            a='b'
                            while a=='b':
                                acc=int(input("Enter your account number:"))
                                sel=("Select * from RECORDS where ACCOUNT_NO={}").format(acc)
                                c1.execute(sel)
                                c1.fetchall()
                                da=c1.rowcount
                                if da==1:
                                    p=int(input("Enter your pincode:-"))
                                    print('========================================================================')
                                    sel1=("Select pincode from RECORDS where ACCOUNT_NO={}").format(acc)
                                    c1.execute(sel1)
                                    a=c1.fetchone()
                                    a1=list(a)

                                i=int(input("Enter your new pincode:"))
                                cb="select * from records where PINCODE={}".format(i)
                                c1.execute(cb)
                                c1.fetchall()
                                data=c1.rowcount
                                if data==1:
                                    print("This pincode already exists")
                                    print("Try again")
                                    
                                    y=input("Do you want to continue y/n -")
                                    if y=="y":
                                        continue
                                    else:
                                        print("Thank you")
                                
                                else:
                                    ar=("UPDATE RECORDS set PINCODE={} where ACCOUNT_NO={}").format(i,acc)
                                    c1.execute(ar)
                                    con.commit()
                                    print('==================================')
                                    print("Your new pincode is ",i)
                                    print('==================================')
                                    y=input("Do You Want To Continue?:")
                                    if y=='Yes' or y=='yes':
                                        continue
                                    else:
                                        print('Thank You')
                                        break

                                    
                        if i==6:
                            print('Logged Out')
                            break                    
                        
                            
        if ch==2:
            print('Thank You Very Much')
            print('Please visit again')
            c1.close()

    if ch==3:
        print('YOU HAVE SUCCESSFULLY EXITED')
        break