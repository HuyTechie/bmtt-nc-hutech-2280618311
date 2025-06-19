# Tornado WebSocket AES Encryption

This project demonstrates a simple WebSocket communication between a client and a server using Tornado. The server encrypts messages received from the client using AES encryption and sends the encrypted messages back to the client.

## Project Structure

```
tornado-websocket-aes
├── src
│   ├── server.py          # WebSocket server implementation
│   ├── client.py          # WebSocket client implementation
│   └── utils
│       └── aes_helper.py  # AES encryption and decryption utilities
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd tornado-websocket-aes
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the WebSocket server:
   ```
   python src/server.py
   ```

2. In a separate terminal, run the WebSocket client:
   ```
   python src/client.py
   ```

3. Follow the prompts in the client to send messages to the server. The server will respond with the encrypted messages.

## Overview of WebSocket Communication

- The client establishes a WebSocket connection to the server.
- The client sends a message to the server.
- The server receives the message, encrypts it using AES, and sends the encrypted message back to the client.
- The client receives the encrypted message and can display or process it as needed.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.