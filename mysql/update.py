import sys
from datetime import datetime
from utils.connection import connection

def update(id):
    cursor = connection.cursor()

    new_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("UPDATE posts SET stamp = %s WHERE id = %s", (new_stamp, id))
    connection.commit()
    cursor.close()
    connection.close()



if __name__ == "__main__":
    id = sys.argv[1]
    update(id)