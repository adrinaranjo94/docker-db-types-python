import pymongo

# If you dont use docker-compose, change localhost to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/pluto")

# Get database
db = client.pluto

# Get collectoins
collection = db.posts
