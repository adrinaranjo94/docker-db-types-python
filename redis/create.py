import sys
from utils.connection import client

def create(key, value):
    client.set(key, value)


if __name__ == "__main__":
    key = sys.argv[1]
    value = sys.argv[2]
    create(key, value)