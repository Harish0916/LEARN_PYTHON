import mysql.connector as c
con = c.connect(
    host="localhost",
    user="root",
    password="123456",
    database="mydatabase"
)
if con.is_connected():
    print("Successfully Connected");
else:
    print("Error to connect with db");
    
