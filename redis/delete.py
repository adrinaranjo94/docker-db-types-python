import sys
from utils.connection import client

def delete(key):
    client.delete(key)

if __name__ == "__main__":
    key = sys.argv[1]
    delete(key)