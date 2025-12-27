from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.api import citizen_api
from app.services.ws_manager import manager

# Create Tables in Supabase
Base.metadata.create_all(bind=engine)

app = FastAPI(title="NagrikAlert Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the Citizen API Router
app.include_router(citizen_api.router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "Active", "system": "NagrikAlert v1.0"}

@app.websocket("/ws/feed")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)