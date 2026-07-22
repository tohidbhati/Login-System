import mysql.connector
# ADDING MYSQL 
connection = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="root",
    database="login_system"
)
cursor = connection.cursor()

connection.autocommit = False

