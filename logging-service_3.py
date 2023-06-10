import asyncio
import uvicorn
import hazelcast
from fastapi import FastAPI
from typing import Dict
import requests
from pydantic import BaseModel

# Hazelcast client configuration
client = hazelcast.HazelcastClient(
    cluster_members=[
        "127.0.0.1:5701"  # Зазначте адреси всіх екземплярів Hazelcast
    ]
)

# Get the Distributed Map from Hazelcast Cluster.
distributed_map = client.get_map("distributed-map")

class Log(BaseModel):
    uuid: str
    msg: str

app = FastAPI()

@app.post("/log")
async def create_log(log: Log):
    await distributed_map.set(log.uuid, log.msg)
    return {'uuid': log.uuid, 'msg': log.msg}

@app.get("/log")
async def get_log():
    all_values = await distributed_map.values()
    return {'logs': all_values}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5006)
