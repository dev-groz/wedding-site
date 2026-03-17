from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

app = FastAPI(
    redoc_url=None,
    docs_url=None,
    openapi_url=None,
    )

@app.get('/')
async def home(request: Request):
    return FileResponse('templates/index.html')

@app.head('/health')
@app.get('/health')
async def health():
    return {'status':'ok'}