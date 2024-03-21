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
sql = 'DELETE FROM student WHERE stuid=103'                # for delete row by given uniqe id
# sql = 'UPDATE student SET FEES=40000 WHERE stuid=104'    # for update in a given id 
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()                                          # In table any chnages or insert or update after it need to save with commit()
    print(myc.rowcount,'Row Deleted')                      # rowcount() property use to tell how much row inserted at a time
    # print(myc.rowcount,'Row Update')                     # for update display
except:
    conn.rollback()                                        # Reverse 1 step
    print('Unable to Insert Data')             

myc.close()
conn.close()