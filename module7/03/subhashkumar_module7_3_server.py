# subhashkumar_module7_3.py

# make python program to POST a FastAPI with server health information and server time time. How can you call the api from another computer. 

from fastapi import FastAPI
from datetime import datetime
import platform

app = FastAPI()


@app.post("/server-health")
def server_health():

    return {
        "status": "healthy",
        "server_time": datetime.now().isoformat(),
        "server_name": platform.node(),
        "operating_system": platform.system()
    }
