import socket
from datetime import datetime
import threading
from cryptography.fernet import Fernet


KEY = 'qzC8_g45d2tW0umj7GHq6ERiJqe3aRdu6NVrhH-9xLY='
HOST = "127.0.0.1"
PORT = 5555

def encrypt_msg(fernet, msg):
    return fernet.encrypt(msg.encode())

def decrypt_msg(fernet, msg):
    return fernet.decrypt(msg).decode()

def close_conn(conn, fernet):
    try:
        conn.send(encrypt_msg(fernet, "#c#c#"))
    except BrokenPipeError:
        print("Client connection already closed")
    finally:
        conn.close()
        print("Connection closed")

def receive_message(conn, fernet):
    while True:
        msg = conn.recv(1024)
        decrypted_msg = decrypt_msg(fernet, msg)
        if decrypted_msg and decrypted_msg != "#c#c#":
            print(datetime.now().strftime("%I:%M:%S"), ">", decrypted_msg)
        else:
            break
    close_conn(conn, fernet)


def start_server(sock, fernet):
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    rm_thread = threading.Thread(target=receive_message, args=(conn, fernet))
    rm_thread.daemon = True
    rm_thread.start()
    while True:
        user_input = input()
        if user_input in ["q", "Q"]:
            break
        enc_msg = encrypt_msg(fernet, user_input)
        conn.send(enc_msg)
    close_conn(conn, fernet)
    
if __name__ == "__main__":
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    fernet = Fernet(KEY)
    try:
        start_server(sock, fernet)
    except (KeyboardInterrupt, EOFError):
        sock.close()

