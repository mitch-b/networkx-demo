from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }