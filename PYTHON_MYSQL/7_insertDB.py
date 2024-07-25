import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="mydatabase1"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Harish", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

# print(mycursor.rowcount, "record inserted.")
print(mycursor.rowcount, " record inserted, ID:", mycursor.lastrowid)
