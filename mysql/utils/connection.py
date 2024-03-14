import mysql.connector

# establish connection
connection = mysql.connector.connect(
    host="localhost",
    password="root_password",
    database="pluto",
    auth_plugin='mysql_native_password'
)
