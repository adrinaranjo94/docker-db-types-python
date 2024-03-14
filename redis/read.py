import sys
from utils.connection import client

def read(key):
    print("value in key:")
    print(client.get(key))

if __name__ == "__main__":
    key = sys.argv[1]
    read(key)