import socket
import threading            
from cryptography.fernet import Fernet
from datetime import datetime


HOST = '127.0.0.1'               
PORT = 5555
KEY = 'qzC8_g45d2tW0umj7GHq6ERiJqe3aRdu6NVrhH-9xLY='
       

def encrypt_msg(fernet, msg):
    return fernet.encrypt(msg.encode())

def decrypt_msg(fernet, msg):
    return fernet.decrypt(msg).decode()

def close_conn(sock, fernet):
    try:
        sock.send(encrypt_msg(fernet, "#c#c#"))
    except OSError:
        print("Server connection already closed")
    finally:
        sock.close()
        print("Connection closed")

def receive_message(sock, fernet):
    while True:
        msg = sock.recv(1024)
        decrypted_msg = decrypt_msg(fernet, msg)
        if decrypted_msg and decrypted_msg != "#c#c#":
            print(datetime.now().strftime("%I:%M:%S"), ">", decrypted_msg)
        else:
            break
    close_conn(sock, fernet)


def start_client(sock, fernet):
    print("type message and press enter or type q or Q to quit")
    sock.connect((HOST, PORT))
    rm_thread = threading.Thread(target=receive_message, args=(sock, fernet))
    rm_thread.daemon = True
    rm_thread.start()
    while True:
        user_input = input()
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