from datetime import datetime
from utils.connection import collection
import uuid

# Create document
id = str(uuid.uuid4())
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

item = {
    'id': id,
    'stamp': time
}

collection.insert_one(item)