# Parametrized Query Insert one row, many row by executemany() method
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

sql = 'INSERT INTO student(name, roll, fees) VALUES(%s, %s, %s)'                 
myc = conn.cursor()
# params = ("Ramu", 110, 65400.90)
params = [("Rakesh", 111, 23100.90), ("Rajat", 112, 34400.90), ("Raju", 113, 44400.90)]
try:
    # myc.execute(sql, params)     # Insert one row 
    myc.executemany(sql, params)   #Insert  many  row by executemany()method
    conn.commit()                                                            
    # print(myc.rowcount, 'Row Inserted') 
    # print(f'Stu ID: {myc.lastrowid} Inserted')   
except:
    conn.rollback()                                        
    print('Unable to Insert Data')             
myc.close()
conn.close()