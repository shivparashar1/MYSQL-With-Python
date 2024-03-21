#Insert single row or multiple row
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

sql = 'INSERT INTO student(name, roll, fees) VALUES("Ram", 105, 37520.70),("Rani", 106, 26440.20)'
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()                           # In table any chnages or insert or update after it need to save with commit()
    print(myc.rowcount,'Row Inserted')      # rowcount() property use to tell how much row inserted at a time
except:
    conn.rollback()                         # Reverse 1 step
    print('Unable to Insert Data')             

myc.close()
conn.close()