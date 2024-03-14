from utils.connection import connection


# Create cursor
cursor = connection.cursor()

# Start Comment if you use `init.sql`
## delete previous db
query = ("DROP DATABASE IF EXISTS `pluto`;")
cursor.execute(query)

## create db
query = ("CREATE DATABASE IF NOT EXISTS pluto")
cursor.execute(query)

##  Use db
query = ("USE pluto")
cursor.execute(query)

## Create table
query = ('''
CREATE TABLE posts(
         id VARCHAR(36),
         stamp VARCHAR(20)
)
''')
cursor.execute(query)
# Finish comment if you use `init.sql`

# Clean up
connection.commit()
cursor.close()
connection.close()