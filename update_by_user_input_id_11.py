# Parametrized User Input Multiple Row
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

sql = 'UPDATE student SET name=%(n)s, roll=%(r)s, fees=%(f)s WHERE stuid=%(i)s'                 
myc = conn.cursor()
id = int(input('Enter Student ID to Update:- '))
nm = input('Enter Name:- ')
ro = int(input('Enter Roll:-'))
fe = float(input('Enter Fees:- '))
update_value = {'n':nm, 'r':ro, 'f':fe, 'i':id}
try:
        myc.execute(sql, update_value)
        conn.commit()
        print(myc.rowcount, 'Row Updated')                                                               
except:
        conn.rollback()                                        
        print('Unable to Insert Data')             
myc.close()
conn.close()