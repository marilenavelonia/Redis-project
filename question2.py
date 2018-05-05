import redis

redis_cli = redis.StrictRedis(host="localhost", port=6379, db=0)

keyslist = []

for key in redis_cli.scan_iter():
    if key not in keyslist:
        keyslist.append(key)
        values = redis_cli.lrange(key, -100, -1)
        sum = 0
        for value in values:
            strvalue = value.decode('ascii')
            flovalue = float(strvalue)
            #value1 = struct.unpack("<L", value)
            sum = sum + flovalue
        length = redis_cli.llen(key)
        avg = sum/length
        print(key.decode('ascii') + ' avg stock price is: ' + str(avg))
