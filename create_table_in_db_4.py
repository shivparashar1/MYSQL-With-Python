#Create a table in db by python program
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

sql = 'CREATE TABLE student(stuid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), roll INT, fees FLOAT)'
# sql = 'SHOW TABLES'               #To show table in terminal after creation
myc = conn.cursor()
myc.execute(sql)               
# for t in myc:                     # show via for loop
#     print(t)

myc.close()
conn.close()