from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.graph.graphservice import GraphService
from app.paths.pathservice import PathService
import networkx as nx

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    graphService = GraphService()
    nodeA = graphService.get_random_node()
    nodeB = graphService.get_random_node()
    return templates.TemplateResponse("index.html", {"request": request, "nodeA": nodeA, "nodeB": nodeB})

@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }

@app.get("/graph/paths/shortest/{origin}/to/{destination}")
async def get_path(request: Request, origin: str, destination: str):
    service = PathService()
    return { 
        "path": service.get_path(origin, destination) 
    }

@app.get("/graph/paths/all/{origin}/to/{destination}")
async def get_path(request: Request, origin: str, destination: str):
    service = PathService()
    return { 
        "paths": service.get_paths(origin, destination) 
    }

@app.get("/graph/paths/shortest/{origin}/to/{destination}/visualize", response_class=HTMLResponse)
async def get_path_visualization(request: Request, origin: str, destination: str):
    service = PathService()
    html_content = service.visualize_path(origin, destination)
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/graph/visualize", response_class=HTMLResponse)
async def get_path_visualization(request: Request):
    service = PathService()
    html_content = service.visualize(service.graphService.get())
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/graph/save-to-file")
async def get_path_visualization(request: Request):
    graphService = GraphService()
    graphService.save_to_file()
    return {}

