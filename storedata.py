import socket
import time
import os
import redis

#connect to redis
redis_cli = redis.StrictRedis(host="localhost", port=6379, db=0)

#create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverip = '46.4.18.132'
port = 1337
client_socket.connect((serverip, port))

#continuously read from stream
while 1:
    data = client_socket.recv(1024)
    data1 = data.decode('ascii')
    data2 = os.linesep.join([s for s in data1.splitlines() if s])
    data3 = data2.split(',')
    data4 = []
    for j in data3:
        data31 = j.split('\r\n')
        data4.extend(data31)
    for i in range(0, len(data4), 2):
        #store data in redis
        redis_cli.rpush(data4[i], data4[i+1])
