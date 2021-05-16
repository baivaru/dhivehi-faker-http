import time

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.background import BackgroundTask
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import StreamingResponse, FileResponse
from faker import DhivehiFaker as BaivaruFaker

app = FastAPI(
    title="Baivaru Faker",
    description="Generate lorem but for Dhivehi",
    version="0.0.1",
)

# Allow all origins CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

templates = Jinja2Templates(directory="templates")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """
    Middleware to include response processing time.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get('/', response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/api/')
async def home():
    return {
        'app': 'BaivaruFaker',
        'description': 'Generate lorem but for Dhivehi',
        'version': '0.0.1',
        'project': 'https://github.com/baivaru/BaivaruFaker',
        'docs': 'https://faker.baivaru.net/docs',
        'available_endpoints': [
            '/api/word',
            '/api/word/{count}',
            '/api/sentence',
            '/api/sentence/{count}',
            '/api/paragraph',
            '/api/paragraph/{count}',
        ]
    }


@app.get("/api/word/{count}")
async def read_item(count: int):
    faker = BaivaruFaker()
    output = faker.words(count, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/api/word")
async def read_item():
    faker = BaivaruFaker()
    output = faker.words(1, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/api/sentence/{count}")
async def read_item(count: int):
    faker = BaivaruFaker()
    output = faker.sentences(count, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/api/sentence")
async def read_item():
    faker = BaivaruFaker()
    output = faker.sentences(1, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/api/paragraph/{count}")
async def read_item(count: int):
    faker = BaivaruFaker()
    output = faker.paragraphs(count, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/api/paragraph")
async def read_item():
    faker = BaivaruFaker()
    output = faker.paragraphs(1, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }
