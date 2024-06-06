import threading
import socket
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Client settings
username = input("Choose a username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))

# GUI setup
window = tk.Tk()
window.title("Chat Room")

# Function to send a message
def send_message():
    message = f'{username}: {msg_entry.get()}'
    client.send(message.encode())
    msg_entry.delete(0, tk.END)

# Function to receive messages
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "username?":
                client.send(username.encode())
            else:
                chat_box.config(state=tk.NORMAL)
                chat_box.insert(tk.END, message + '\n')
                chat_box.config(state=tk.DISABLED)
                chat_box.yview(tk.END)
        except:
            print("An error occurred!")
            client.close()
            break

# Setting up the GUI layout
chat_box = scrolledtext.ScrolledText(window, state=tk.DISABLED)
chat_box.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

msg_entry = tk.Entry(window, width=50)
msg_entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Function to close the application safely
def on_closing():
    try:
        client.send(f'{username} has left the chat room.'.encode())
        client.close()
    except:
        pass
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

# Start receiving thread
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Run the GUI event loop
window.mainloop()
