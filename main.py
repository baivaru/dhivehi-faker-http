import time

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.middleware.cors import CORSMiddleware

from faker import DhivehiFaker as BaivaruFaker

limiter = Limiter(key_func=get_remote_address)

limiter.enabled = True

app = FastAPI(
    title="Baivaru Faker",
    description="Generate lorem but for Dhivehi",
    version="0.0.1",
)

app.state.limiter = limiter

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

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


@app.get("/api/word")
@limiter.limit('100/min')
async def single_word(request: Request):
    faker = BaivaruFaker()
    output = faker.words(1, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/api/word/{count}")
@limiter.limit('1/min')
async def multi_word(request: Request, count: int):
    faker = BaivaruFaker()
    output = faker.words(count if count < 10 else 10, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/api/sentence")
@limiter.limit('100/min')
async def single_sentence(request: Request):
    faker = BaivaruFaker()
    output = faker.sentences(1, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/api/sentence/{count}")
@limiter.limit('100/min')
async def multi_sentence(request: Request, count: int):
    faker = BaivaruFaker()
    output = faker.sentences(count if count < 10 else 10, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/api/paragraph")
@limiter.limit('100/min')
async def single_paragraph(request: Request):
    faker = BaivaruFaker()
    output = faker.paragraphs(1, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/api/paragraph/{count}")
@limiter.limit('100/min')
async def multi_paragraph(request: Request, count: int):
    faker = BaivaruFaker()
    output = faker.paragraphs(count if count < 10 else 10, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }
