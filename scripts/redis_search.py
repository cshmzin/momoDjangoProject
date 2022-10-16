from redis import Redis

r = Redis(db=1)
print(r.keys())