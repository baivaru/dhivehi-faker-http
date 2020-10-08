from fastapi import FastAPI

from FakerAPI.BaivaruFaker import BaivaruFaker

app = FastAPI(
    title="Baivaru Faker",
    description="Generate lorem but for Dhivehi",
    version="0.0.1",
)


@app.get('/')
async def home():
    return {
        'app': 'BaivaruFaker',
        'description': 'Generate lorem but for Dhivehi',
        'version': '0.0.1',
        'project': 'https://github.com/baivaru/BaivaruFaker',
        'docs': 'https://faker.baivaru.net/docs',
        'available_endpoints': [
            '/word',
            '/word/{count}',
            '/sentence',
            '/sentence/{count}',
            '/paragraph',
            '/paragraph/{count}',
        ]
    }


@app.get("/word/{count}")
async def read_item(count: int):
    faker = BaivaruFaker()
    output = faker.words(count, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/word")
async def read_item():
    faker = BaivaruFaker()
    output = faker.words(1, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/sentence/{count}")
async def read_item(count: int):
    faker = BaivaruFaker()
    output = faker.sentences(count, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/sentence")
async def read_item():
    faker = BaivaruFaker()
    output = faker.sentences(1, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/paragraph/{count}")
async def read_item(count: int):
    faker = BaivaruFaker()
    output = faker.paragraphs(count, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }


@app.get("/paragraph")
async def read_item():
    faker = BaivaruFaker()
    output = faker.paragraphs(1, True)

    return {
        "full": ' '.join(output),
        "raw": output,
    }
