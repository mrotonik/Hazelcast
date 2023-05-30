import asyncio
import uvicorn
import hazelcast
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import requests
import uuid

# Hazelcast client configuration
client = hazelcast.HazelcastClient(
    cluster_members=[
        "127.0.0.1:5701"
    ]
)

# Get the Distributed Map from Hazelcast Cluster.
distributed_map = client.get_map("distributed-map")

class Message(BaseModel):
    msg: str

app = FastAPI()

@app.post("/message")
async def create_message(message: Message):
    unique_id = str(uuid.uuid4())
    await distributed_map.set(unique_id, message.msg)
    requests.post('http://localhost:8001/log', data = {'uuid':unique_id, 'msg':message.msg})
    return {'UUID':unique_id, 'msg':message.msg}

@app.get("/message")
async def get_message():
    all_values = await distributed_map.values()
    messages_response = requests.get('http://localhost:8002/message')
    return {'logs': all_values, 'message': messages_response.text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
