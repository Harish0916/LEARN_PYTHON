import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers");
mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()
# myresult = mycursor.fetchone()

for x in myresult:
  print(x)