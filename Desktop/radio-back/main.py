import uvicorn as uvicorn
from fastapi import FastAPI
from radio_backend import RadioBackend
app = FastAPI()

radio_backend = RadioBackend()

@app.get("/")
async def get_radios():
    return radio_backend.get_radios()

if __name__ == "__main__":
    uvicorn.run(app)