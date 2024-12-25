# import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# Server connection details
HOST = '127.0.0.1'
PORT = 1234

# GUI colors and fonts
DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)

# Creating a socket object
# AF_INET: we are going to use IPv4 addresses
# SOCK_STREAM: we are using TCP packets for communication
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def add_message(message):
    """Add a message to the message box."""
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)

def connect():
    """Connect to the server and start listening for messages."""
    try:
        # Connect to the server
        client.connect((HOST, PORT))
        print("Successfully connected to server")
        add_message("[SERVER] Successfully connected to the server")
    except socket.error as e:
        messagebox.showerror("Unable to connect to server", f"Unable to connect to server {HOST} {PORT}\n{e}")
        return

    username = username_textbox.get()
    if username:
        client.sendall(username.encode())
    else:
        messagebox.showerror("Invalid username", "Username cannot be empty")
        return

    threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()

    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)

def send_message():
    """Send a message to the server."""
    message = message_textbox.get()
    if message:
        client.sendall(message.encode())
        message_textbox.delete(0, tk.END)
    else:
        messagebox.showerror("Empty message", "Message cannot be empty")

def listen_for_messages_from_server(client):
    """Listen for messages from the server."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                add_message(message)
            else:
                client.close()
                break
        except Exception as e:
            print(f"Error: {e}")
            client.close()
            break

# GUI setup
root = tk.Tk()
root.title("Chat Application")
root.geometry("600x400")
root.resizable(False, False)
root.configure(bg=MEDIUM_GREY)

# Message display frame
message_frame = tk.Frame(root, bg=MEDIUM_GREY)
message_frame.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

message_box = scrolledtext.ScrolledText(message_frame, font=SMALL_FONT, bg=DARK_GREY, fg=WHITE, width=50, height=15)
message_box.config(state=tk.DISABLED)
message_box.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

# Username input frame
username_frame = tk.Frame(root, bg=MEDIUM_GREY)
username_frame.pack(padx=20, pady=5, fill=tk.X)

username_label = tk.Label(username_frame, text="Enter username:", font=FONT, bg=MEDIUM_GREY, fg=WHITE)
username_label.pack(side=tk.LEFT, padx=5)

username_textbox = tk.Entry(username_frame, font=FONT, bg=DARK_GREY, fg=WHITE)
username_textbox.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

username_button = tk.Button(username_frame, text="Join", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=connect)
username_button.pack(side=tk.LEFT, padx=5)

# Message input frame
message_frame = tk.Frame(root, bg=MEDIUM_GREY)
message_frame.pack(padx=20, pady=5, fill=tk.X)

message_textbox = tk.Entry(message_frame, font=FONT, bg=DARK_GREY, fg=WHITE, width=38)
message_textbox.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

message_button = tk.Button(message_frame, text="Send", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=send_message)
message_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()