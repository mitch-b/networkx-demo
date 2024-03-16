from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_items():
    html_content = """
    <html>
        <head>
            <title>NetworkX Demo</title>
        </head>
        <body>
            <h1>Demos</h1>
            <ul>
              <li><a href="/hello/world">/hello/world</a></li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }