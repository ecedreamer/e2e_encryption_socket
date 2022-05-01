import socket            
from cryptography.fernet import Fernet


HOST = '127.0.0.1'               
PORT = 5555
KEY = 'qzC8_g45d2tW0umj7GHq6ERiJqe3aRdu6NVrhH-9xLY='
       



def encrypt_msg(fernet, msg):
    return fernet.encrypt(msg.encode())

def close_conn(sock, fernet):
    sock.send(encrypt_msg(fernet, "#c#c#"))
    sock.close() 
    print("Connection closed")

def start_client(sock, fernet):
    print("type message and press enter or type q or Q to quit")
    sock.connect((HOST, PORT))
    while True:
        user_input = input("> ")
        if user_input in ["q", "Q"]:
            break
        enc_msg = encrypt_msg(fernet, user_input)
        sock.send(enc_msg)
    close_conn(sock, fernet)


if __name__ == "__main__":
    sock = socket.socket()
    fernet = Fernet(KEY)
    try:
        start_client(sock, fernet)
    except (KeyboardInterrupt, EOFError):
        close_conn(sock, fernet)