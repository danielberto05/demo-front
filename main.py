from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from functions import get_info

import os

BACK_END_URL = os.getenv('BACK_END_URL')
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def start_page(request: Request):
    return templates.TemplateResponse("index.html", 
                                      {
                                          "request": request,
                                          "clients_table": await get_info.get_client(),
                                          "products_table": await get_info.get_products(),
                                          "back_url": BACK_END_URL,
                                      })
