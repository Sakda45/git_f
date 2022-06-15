import mysql.connector

def con() :
    mydb = mysql.connector.connect(
    host="localhost",
    user="test_1",
    password="12345",
    database="test_1"
)
    return mydb

class con2:
    def getHW2():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hw "
        mycursor.execute(sql) 
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def getHW_onlyName():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT name, hw_name FROM hw "
        mycursor.execute(sql) 
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getHW_minData():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hw WHERE id = (SELECT MIN(id) FROM hw)"
        mycursor.execute(sql) 
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    
    def getHWid(id):
        
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM users WHERE id = {}".format(id)
        mycursor.execute(sql) 
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
     
    def insert_data(name, hw_name, status,value):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO hw (name, hw_name, status,value) VALUE ('{}','{}', '{}',{})".format(
            name, hw_name, status,value
        )
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.fetchall()
        return ID
    
    def update_hw(id,status,value):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hw SET status = '{}', value = {} WHERE id = {}".format(
            status,value,id
            )
        mycursor.execute(sql)
        mydb.commit()  
        return {'trun'}
    
    def update_users(id,name,last_name):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE users SET name = '{}', last_name = '{}' WHERE id = {}".format(
            name,last_name,id
            )
        mycursor.execute(sql)
        mydb.commit()  
        return {'trun'}
    
    def delete_hw_maxData(data):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM hw WHERE id = (SELECT {}(id) FROM hw)".format(
            data
        )
        mycursor.execute(sql)
        mydb.commit()