#Delete , Update in Table In python
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
# sql = 'DELETE FROM student WHERE stuid=%s'    # to Delete single row with Where clause by user input choice id
sql = 'SELECT * FROM student WHERE stuid=%s'    # to Retrieve single row with WHERE clause by user input          
myc = conn.cursor()
# n = int(input('Enter ID to Delete:-'))        # take input to delete id from user
n = int(input('Enter Student ID to Display:- ')) # ID input which one is Retrieve
# del_value=(n,)
disp_value = (n,)
try:
    # myc.execute(sql, del_value)                # execute query for Delete
    # conn.commit()                                          
    # print(myc.rowcount,'Row Deleted')    
     
    myc.execute(sql, disp_value)                 # execute query for retrieve
    row = myc.fetchone()                         #fetch data
    print(row)                      
    print('Total Row:', myc.rowcount)           
except:
    # conn.rollback()                                       
    # print('Unable to Delete Data') 
    # print('Unable to Display Data')
    print('Unable to Retrieve Data')             #Display when get error
myc.close()
conn.close()