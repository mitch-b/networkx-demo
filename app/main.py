from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.paths.pathservice import PathService
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
async def get_path(request: Request, origin: str, destination: str):
    service = PathService()
    return { 
        "path": service.get_path(origin, destination) 
    }

@app.get("/graph/paths/{origin}/to/{destination}/visualize", response_class=HTMLResponse)
async def get_path_visualization(request: Request, origin: str, destination: str):
    service = PathService()
    html_content = service.visualize_path(origin, destination)
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/graph/visualize", response_class=HTMLResponse)
async def get_path_visualization(request: Request):
    service = PathService()
    html_content = service.visualize(service.graphService.get())
    return HTMLResponse(content=html_content, status_code=200)

