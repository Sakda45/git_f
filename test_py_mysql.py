import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="test_1",
    password="12345",
    database="test_1"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM hw"

mycursor.execute(sql)

data = mycursor.fetchall()


#for x in myresult:
 #  print(x)

print(data[0][1])