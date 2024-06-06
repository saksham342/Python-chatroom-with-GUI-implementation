import threading
import socket

host = 'localhost'
port = 55555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f"{username} has left the chat room".encode())
            usernames.remove(username)
            break
    
def receive():
    while True:
        print("[+] The server is running .....")
        client, address = server.accept()
        print(f"The connection is established with {str(address)}")
        client.send("username?".encode())
        username = client.recv(1024).decode()
        usernames.append(username)
        clients.append(client)
        print(f"The username of the client is : {username}")
        broadcast(f"{username} has connected the chatroom".encode())
        client.send("You are now connected.".encode())
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
