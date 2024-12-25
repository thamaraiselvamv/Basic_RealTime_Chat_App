# Basic_RealTime_Chat_App
The Basic Real-Time Chat Application is a Python console app that allows users to join a group chat, send messages, and see real-time updates using socket programming, without message persistence.


The Basic Real-Time Chat Application is a console-based Python application that enables multiple users to communicate in a group chat room using socket programming. Users can connect to the server, enter a username, and send messages that are instantly broadcast to all participants. The application features a simple command-line interface, displaying messages with the sender's username. It does not store messages persistently, focusing solely on real-time communication. This lightweight application serves as a foundational project for understanding network programming in Python and can be expanded with features like message persistence and user authentication in the future.



Socket Server

A server-side application that listens for incoming client connections and manages communication between clients.
Handles broadcasting messages to all connected clients in the chat room.
Client Application

A Python script that connects to the chat server using sockets.
Handles user input for sending messages and displays incoming messages from other users.
No Database Required

For this basic implementation, messages are not stored persistently; they exist only in memory while the server is running.
This keeps the application lightweight and focused on real-time communication.



Group Chat Functionality

Users can join a common chat room where all messages are visible to everyone in the room.
Supports multiple users participating in the same conversation simultaneously.
Real-Time Messaging

Messages are sent and received instantly using WebSocket technology, ensuring that all participants see new messages as they are posted.
Users can type messages and hit "send" to communicate with the group.
User Interface (UI)

A clean and simple chat window that displays all messages in chronological order.
An input field at the bottom of the chat window for users to type their messages.
A list of active users (optional) to show who is currently in the chat room.
Basic User Management

Users can enter a username when joining the chat room, which will be displayed alongside their messages.
Users can leave the chat room at any time.
Message Display

Each message shows the sender's username and the message content.
Messages are displayed in a scrollable area, allowing users to view the chat history.
