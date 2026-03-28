from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse

from sheets_service import write_to_sheet

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
    write_to_sheet(first_name, last_name, phone)
    return RedirectResponse('/')


@app.head('/health')
@app.get('/health')
async def health():
    return {'status':'ok'}