import sys
from utils.connection import connection

def delete(id):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM posts WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()



if __name__ == "__main__":
    id = sys.argv[1]
    delete(id)