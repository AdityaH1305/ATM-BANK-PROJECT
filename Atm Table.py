import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='12345',database='ATM_MACHINE')
if con.is_connected():
      print("Sucessfully Connected")
c1=con.cursor()
db="CREATE TABLE RECORDS( ACCOUNT_NO  INT(4) primary key,PINCODE INT(3),NAME VARCHAR(20),CR_AMOUNT INT (6),WITHDRAWAL INT (6) default 0 ,BALANCE INT (6))"
c1.execute(db)
print("Sucessfully Created")