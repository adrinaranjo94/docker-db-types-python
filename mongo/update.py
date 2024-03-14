import sys
from datetime import datetime
from utils.connection import collection

def update(id):
    idToUpdate = {"id": id}
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    collection.update_one(idToUpdate, {"$set": {"stamp": time}})



if __name__ == "__main__":
    id = sys.argv[1]
    update(id)