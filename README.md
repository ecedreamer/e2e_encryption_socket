**SIMPLE SOCKET PROGRAMMING USING END TO END ENCRYPTION**

This is simple python example which uses end to end symmetric encryption for communication. This example uses socket programming in python for networking.
In this example, client can send the encrypted message and server receives the encrypted message,  decrypt it and print it in console.  

You need a cryptography library

    pip install cryptography


To run server:

    python3 server/server.py

To run client:

    python3 client/client.py


Now you can send message from client to server which is encrypted. 

You need to share same key to both the client and server in symmetric encryption. 

References: 

    1. https://cryptography.io/en/latest/ 
    
    2. https://docs.python.org/3/howto/sockets.html
