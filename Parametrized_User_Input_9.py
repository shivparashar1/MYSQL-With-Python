# Parametrized User Input Multiple Row
import mysql.connector
def student_data(nm,ro,fe):
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
    n = nm 
    r = ro
    f = fe 
    params = (n,r,f)
    try:
        myc.execute(sql, params)
        conn.commit()
        print(myc.rowcount, 'Row Inserted')
        print(f'StuId: {myc.lastrowid} Inserted')                                                               
    except:
        conn.rollback()                                        
        print('Unable to Insert Data')             
    myc.close()
    conn.close()
while True:
    nm = input('Enter Name:- ')
    ro = int(input('Enter Roll no:- '))
    fe = float(input('Enter Fees:- '))
    student_data(nm, ro, fe)
    ans = input('Do you want to exit?(y/n)')
    if (ans =='y'):
        break