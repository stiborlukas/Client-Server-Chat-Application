# &#x20;Client-Server Chat Application

A basic **Client-Server Chat Application** built using Python's `socket` module for networking, `tkinter` for the GUI, and `customtkinter` for enhanced user experience. It supports real-time messaging, private messaging, and simple chat commands, with the potential for **End-to-End Encryption (E2EE)** as a future enhancement.

## Features

### Server Side (Backend)

- **Socket Setup**:

  - Listens for incoming connections on `127.0.0.1:9090`.
  - Assigns a unique nickname to each client upon connection.

- **Client Management**:

  - **Broadcasting**: Messages sent to all connected clients.
  - **Private Messaging**: Send messages to specific users by typing `@username`.
  - **Commands**:
    - `/help`: Show available commands.
    - `/users`: List all online users.
    - `/clear`: Clear the client’s chat window.
  - **Nickname Handling**: Ensures unique nicknames by appending a suffix if necessary (e.g., `nickname_1`).

- **Logging**:

  - Logs server events and errors to `server_logs.log` with timestamps and error details.

- **Concurrency**:

  - Manages multiple clients in separate threads for simultaneous connections.

### Client Side (Frontend)

- **Tkinter and CustomTkinter GUI**:

  - User-friendly interface includes:
    - A chat display area for messages.
    - An input area for typing messages.
    - A send button and a `Ctrl+Enter` shortcut for quick sending.

- **Messaging**:

  - **Sending**: Users can type and send messages.
  - **Receiving**: Messages from the server update the chat display in real-time.

- **Nickname Assignment**:

  - Prompts for a nickname upon startup, ensuring unique names.

- **Graceful Exit**:

  - Closes the server connection and shuts down the application when the user exits.

## How It Works

### Server

1. Accepts client connections and assigns a unique nickname.
2. Manages real-time communication by broadcasting or sending private messages.
3. Supports commands (`/help`, `/users`, `/clear`) for enhanced user interaction.
4. Logs client activities and errors.

### Client

1. Connects to the server and displays real-time messages in a Tkinter GUI.
2. Supports private messaging using `@username`.
3. Provides chat commands for viewing users, clearing the chat, and accessing help.
4. Handles server connection gracefully, including disconnections and errors.

## Key Features

- **Multi-client Support**: Each client is handled in a separate thread.
- **Private Messaging**: Allows direct communication between users.
- **Command System**: Provides a simple way to access chat functionalities.
- **Enhanced GUI**: CustomTkinter provides a modern, responsive interface.
- **Real-time Updates**: Ensures all messages are updated across clients instantly.

## Possible Enhancements

- **End-to-End Encryption (E2EE)** for secure communication.
- **Media Sharing** for images or files.
- **TLS/SSL Encryption** to secure network communication.
- **Improved Error Handling** for network issues and disconnections.
- **User Authentication** for enhanced security and permissions.

## Requirements

- Python 3.x
- `customtkinter` library
- `socket` module (Python standard library)

## Running the Application

### Server

1. Open a terminal window and navigate to the server script location.
2. Run the server script:
   ```bash
   python server.py
   ```

### Client

1. Open a new terminal window and navigate to the client script location.
2. Run the client script:
   ```bash
   python client.py
   ```
3. Enter a nickname when prompted and start chatting.

## Folder Structure

```
project-folder/
├── server.py          # Server-side implementation
├── client.py          # Client-side implementation
├── gui.py             # CustomTkinter GUI implementation
├── server_logs.log    # Log file for server events
├── README.md          # Documentation file
```