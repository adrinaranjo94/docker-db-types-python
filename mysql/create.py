from datetime import datetime
from utils.connection import connection
import uuid
cursor = connection.cursor()

id = str(uuid.uuid4())
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
query= (f'INSERT INTO `posts` VALUES("{id}","{time}")')

cursor.execute(query)
connection.commit()
cursor.close()
connection.close()
