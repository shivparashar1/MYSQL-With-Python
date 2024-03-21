#Create a database by python in db

import mysql.connector
try:
    conn=mysql.connector.connect(
        user = 'root',
        password = 'Admin@123',
        host = 'localhost',
        port = 3306
   )
    if (conn.is_connected):         # check is it connected or not
        print('Connected')

except:
    print('Unable To Connect')

sql = 'CREATE DATABASE pythondb'    #create db in database 'pythondb'
# sql = 'SHOW DATABASES'            # to check in terminal is db created or not
myc = conn.cursor()                 # create cursor object
myc.execute(sql)
# for d in myc:                     # check via for loops bcz there are many db so that access one by one
#     print(d)

myc.close()                         # close cursor
conn.close()                        # close connection