from utils.connection import connection

cursor = connection.cursor()
cursor.execute("SELECT * FROM posts")
rows = cursor.fetchall()

print("rows in pluto`s table:")

for row in rows:
    print(row)
    
cursor.close()
connection.close()