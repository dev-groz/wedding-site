from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/')
async def home(request: Request):
    return FileResponse('templates/index.html')