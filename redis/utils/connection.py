from redis import Redis

client = Redis(host='localhost', port=6379, decode_responses= True)