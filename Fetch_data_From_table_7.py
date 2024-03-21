# Retrieve Row one by one , by Fetchone() Method
import mysql.connector
try:
    conn=mysql.connector.connect(
        user = 'root',
        password = 'Admin@123',
        host = 'localhost',
        database ='pythondb',  
        port = 3306
   )
    if (conn.is_connected):
        print('Connected')

except:
    print('Unable To Connect')

sql = 'SELECT * FROM student'                 
# sql = 'SELECT name,roll FROM student'        # if you want selected column then give name,roll
# myc = conn.cursor(bufferrd=True)             # mention buffered=True for use fetchmany(size=2),Method
myc = conn.cursor()
try:
    myc.execute(sql) 
    rows = myc.fetchone()                       # fetch next row return single sequence
    while rows is not None:                     # by applying while loop we fetch one by one row
        print(rows)
        rows = myc.fetchone()                                         
    print('Total Rows:', myc.rowcount)    

    # rows = myc.fetchall()                     # Here we use Fetchall()method to fetch all rows one bye one 
    # for r in rows:
    #     print(r)  
    # print('Total Rows:', myc.rowcount)         

    # rows = myc.fetchmany(size=5)              # Here we use Fetchmany()method to fetch rows by given no of rows,(size=...)
    # for r in rows:
    #     print(r)  
    # print('Total Rows:', myc.rowcount)         
    
    
except:
    conn.rollback()                                        
    print('Unable to Show Data')             

myc.close()
conn.close()