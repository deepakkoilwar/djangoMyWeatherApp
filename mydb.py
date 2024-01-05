# install musql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python



import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE Weather")

print("Database Connected to app")