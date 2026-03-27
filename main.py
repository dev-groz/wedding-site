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

@app.get('/send_info')
async def send_info(first_name: str, last_name: str, phone: str):
    print({'first_name': first_name, 'last_name': last_name, 'phone': phone})
    return "ok"

@app.head('/health')
@app.get('/health')
async def health():
    return {'status':'ok'}