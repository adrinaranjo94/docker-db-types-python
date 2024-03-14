from utils.connection import collection

for post in collection.find():
    print(post)