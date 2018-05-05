import redis

#connect to redis
redis_cli = redis.StrictRedis(host="localhost", port=6379, db=0)

keyslist = []

#for every key
for key in redis_cli.scan_iter():
    if key not in keyslist:
        keyslist.append(key)
        values = redis_cli.lrange(key, 0, -1)
        sum = 0
        #for every value of the key
        for value in values:
            strvalue = value.decode('ascii')
            flovalue = float(strvalue)
            sum = sum + flovalue
        length = redis_cli.llen(key)
        avg = sum/length
        print(key.decode('ascii') + ' avg stock price is: ' + str(avg))
