# Python-chatroom-with-GUI-implementation
A real-time chat room application using Python with socket programming and a Tkinter-based GUI.

Chat Room Application
This is a simple chat room application using Python's socket and threading libraries for networking and concurrency, and tkinter for the GUI. The application includes both a server and a client. Multiple clients can connect to the server and communicate with each other in real-time.

**Features**

Multi-client Support: Multiple clients can join the chat room and communicate with each other.

Broadcast Messages: Messages from any client are broadcasted to all connected clients.

User Notifications: The server notifies all clients when a new user joins or leaves the chat room.

Graphical User Interface: The client application has a user-friendly GUI for sending and receiving messages.


**Requirements**

Python 3.x

tkinter library (comes pre-installed with Python)

threading library (comes pre-installed with Python)

socket library (comes pre-installed with Python)


**How to Run**

_Server_

Run the server script: python server.py
_Client_

Run the client script: python client1.py and python client2.py for CLI on separate terminals. For GUI, run python GUI_client3.py and python GUI_client4.py on separate terminals

Note: Run both client code, either of two CLI's or two GUI's

Enter a username when prompted.

Use the GUI to send and receive messages.

**Usage**

a. Start the Server: Run server.py to start the server. The server will wait for clients to connect.

b. Connect the Client: Run two client files either CLI type or GUI type, enter your username, and start chatting.

**Notes**

a. Ensure that the server is running before starting any clients.

b. The server and client must be able to connect to each other through the specified host and port.

c. The GUI will help users send and receive messages in a more user-friendly manner compared to the command line.

d. This chat room application is a simple demonstration of network programming and GUI development in Python. It can be extended with more features like private messaging, user authentication, message encryption, etc.

