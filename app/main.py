from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.graph.service import GraphService
import networkx as nx

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }

@app.get("/graph/paths/{origin}/to/{destination}")
async def get_path(origin: str, destination: str):
    service = GraphService()
    graph = service.get()
    try:
        path = nx.shortest_path(graph, origin, destination)
        return {"path": path}
    except nx.NetworkXNoPath:
        return {"error": "No path between these nodes"}