# Redis-project

You are going to use Redis to store a financial data stream and answer stream queries (though not continuous). 


Use the programming language of your choice (e.g. Java, Python), as long as there is an API for Redis in that language, i.e. a set of methods so your programming language can communicate with a Redis server.


Install Redis - it is available for Linux and Mac - and there is a Windows version as well.


Use the financial data stream that exists at IP: 46.4.18.132 and Port: 1337
This a synthetic stream that provides a feed of stock prices in the form: <stockID, price>

storedata.py file: Write a program that uses sockets, connects to the server mentioned above, reads in continuously the stream and stores values per stock id to Redis. But: you should store values in an appropriate data structure to support the programs in 4 and 5.

question1.py file: Write a program that reads in from Redis and prints out for each stock id the average price since the starting point of storing the data stream.

question2.py file: Write a program that reads in from Redis and prints out for each stock id the average price of the last 100 prices (a sliding counting window of size 100).
