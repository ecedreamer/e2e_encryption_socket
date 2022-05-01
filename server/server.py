import socket
from datetime import datetime
from cryptography.fernet import Fernet


KEY = 'qzC8_g45d2tW0umj7GHq6ERiJqe3aRdu6NVrhH-9xLY='
HOST = "127.0.0.1"
PORT = 5555


def decrypt_msg(fernet, msg):
    return fernet.decrypt(msg).decode()

def close_conn(conn):
    conn.close()
    print("Connection closed")

def client_thread(conn, addr):
    while True:
        msg = conn.recv(1024)
        decrypted_msg = decrypt_msg(fernet, msg)
        if decrypted_msg and decrypted_msg != "#c#c#":
            print(datetime.now().strftime("%I:%M:%S"), ">", decrypted_msg)
        else:
            break
    close_conn(conn)


def start_server(sock, fernet):
    sock.bind((HOST, PORT))
    sock.listen(2)
    conn, addr = sock.accept()

    while True:
        msg = conn.recv(1024)
        decrypted_msg = decrypt_msg(fernet, msg)
        if decrypted_msg and decrypted_msg != "#c#c#":
            print(datetime.now().strftime("%I:%M:%S"), ">", decrypted_msg)
        else:
            break
    close_conn(conn)
    
    
if __name__ == "__main__":
    sock = socket.socket()
    fernet = Fernet(KEY)
    try:
        start_server(sock, fernet)
    except (KeyboardInterrupt, EOFError):
        close_conn(sock)

