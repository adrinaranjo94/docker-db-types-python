import sys
from utils.connection import collection

def delete(id):
    idToDelete = {"id": id}
    collection.delete_one(idToDelete)



if __name__ == "__main__":
    id = sys.argv[1]
    delete(id)