import threading
import socket
username = input("Chose an username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "username?":
                client.send(username.encode())
            else: 
                print(message)
        except:
            print("An error occured !")
            client.close()
            break

def client_send():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode())

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
