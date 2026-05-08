from fastapi import WebSocket, WebSocketDisconnect
from app.llm import get_ai_response

class ConnectionManager:

    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

manager = ConnectionManager()

async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:
        while True:

            user_message = await websocket.receive_text()

            # print(f"User: {user_message}")

            ai_response = get_ai_response(user_message)

            # print(f"AI: {ai_response}")

            await manager.send_message(ai_response, websocket)

    except WebSocketDisconnect:

        manager.disconnect(websocket)

        print("Client disconnected")