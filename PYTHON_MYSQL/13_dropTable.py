import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="mydatabase"
)

mycursor = mydb.cursor()

# sql = "DROP TABLE customers"
sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)
