# Import required modules
import socket
import threading

HOST = '127.0.0.1'
PORT = 1234 # You can use any port between 0 to 65535
LISTENER_LIMIT = 5
active_clients = [] # List of all currently connected users

def listen_for_messages(client, username):
    """Listen for incoming messages from a client."""
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message:
                final_msg = username + '~' + message
                send_messages_to_all(final_msg)
            else:
                print(f"The message sent from client {username} is empty")
        except Exception as e:
            print(f"Error: {e}")
            remove_client(client)
            break

def send_message_to_client(client, message):
    """Send a message to a single client."""
    try:
        client.sendall(message.encode())
    except Exception as e:
        print(f"Error: {e}")
        remove_client(client)

def send_messages_to_all(message):
    """Send a new message to all connected clients."""
    for user in active_clients:
        send_message_to_client(user[1], message)

def remove_client(client):
    """Remove a client from the active clients list."""
    for user in active_clients:
        if user[1] == client:
            active_clients.remove(user)
            break

def client_handler(client):
    """Handle a new client connection."""
    while True:
        try:
            username = client.recv(2048).decode('utf-8')
            if username:
                active_clients.append((username, client))
                prompt_message = "SERVER~" + f"{username} joined the chat"
                send_messages_to_all(prompt_message)
                break
            else:
                print("Received empty username")
        except Exception as e:
            print(f"Error: {e}")
            break

    threading.Thread(target=listen_for_messages, args=(client, username)).start()

def main():
    """Main function to start the server."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST, PORT))
        server.listen(LISTENER_LIMIT)
        print(f"Server started on {HOST}:{PORT}")
    except Exception as e:
        print(f"Error: {e}")
        return

    while True:
        client, address = server.accept()
        print(f"Connected with {address}")
        threading.Thread(target=client_handler, args=(client,)).start()

if __name__ == "__main__":
    main()