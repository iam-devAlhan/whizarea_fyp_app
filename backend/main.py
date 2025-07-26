from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def start_server():
    return {"message": "Server running on Port 8000"}