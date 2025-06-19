import asyncio
import websockets

async def send_message(message):
    uri = "ws://localhost:8888/websocket"  # Đúng endpoint WebSocket server
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received encrypted message: {response}")

if __name__ == "__main__":
    message = input("Enter a message to send to the server: ")
    asyncio.run(send_message(message))