from tornado import websocket, web, ioloop
import json
from utils.aes_helper import encrypt_message

class WebSocketHandler(websocket.WebSocketHandler):
    clients = set()

    def open(self):
        self.__class__.clients.add(self)
        print("Client connected")

    def on_message(self, message):
        print(f"Received message: {message}")
        try:
            encrypted_message = encrypt_message(message)
            self.write_message(json.dumps({"encrypted": encrypted_message}))
        except Exception as e:
            self.write_message(json.dumps({"error": str(e)}))

    def on_close(self):
        self.__class__.clients.remove(self)
        print("Client disconnected")

def make_app():
    return web.Application([
        (r"/websocket", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("WebSocket server is running on ws://localhost:8888/websocket")
    ioloop.IOLoop.current().start()