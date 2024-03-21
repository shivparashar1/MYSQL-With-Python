#Create a database by python in db
import mysql.connector
try:
    conn=mysql.connector.connect(
        user = 'root',
        password = 'Admin@123',
        host = 'localhost',
        database ='pythondb',   # in which db you want intract, Mention name here
        port = 3306
   )
    if (conn.is_connected):
        print('Connected')

except:
    print('Unable To Connect')

conn.close()