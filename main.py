from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MeRequest(BaseModel):
    user: str

@app.post("/auth/me")
async def auth_me(payload: MeRequest):
    # retorna exatamente no formato pedido
    return {"user": payload.user, "ping": "pong"}

@app.get("/")
async def root():
    return {"ok": True}
