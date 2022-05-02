**SIMPLE SOCKET PROGRAMMING USING END TO END ENCRYPTION**
This is simple python example which uses end to end symmetric encryption for communication. This example uses socket programming in python for networking.
In this example, both client and server can send and receive encrypted message, decrypt it and print it in the respective console.

You need a cryptography library
    pip install cryptography


To run server:
    python3 server/server.py

To run client:
    python3 client/client.py


Now you can send message from client to server or vice versa which is encrypted. 

You need to share same key to both the client and server in symmetric encryption. 

Reference: 
    1. https://cryptography.io/en/latest/ 
    2. https://docs.python.org/3/howto/sockets.html
    3. https://docs.python.org/3/library/threading.html