# Format of Connection To database
import mysql.connector
try:
    conn=mysql.connector.connect(
        user = 'root',
        password = 'Admin@123',
        host = 'localhost',
        port = 3306
   )
    if (conn.is_connected):
        print('Connected')

except:
    print('Unable To Connect')