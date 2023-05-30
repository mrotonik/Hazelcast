import asyncio
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/message")
async def get_message():
    return {'msg': 'not implemented yet'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5002)
