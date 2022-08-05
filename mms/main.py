from fastapi import FastAPI, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pathlib import Path

from mms.core.config import settings
from mms.api.v1 import api_router
from mms.db import engine
from mms.init_app import main as init_app

BASE_PATH = Path(__file__).resolve().parent # Directory of main.py
ROOT_PATH = BASE_PATH.parent                # Root project directory

# Include Jinja2Templates for template responses
TEMPLATES = Jinja2Templates(directory=f"{BASE_PATH}/templates") 
# usage: return TEMPLATES.TemplateResponse(template_file_name: str, data: dict)

app = FastAPI()
init_app()

root_router = APIRouter()

# Set a home route
@root_router.get('/')
def home():
    return RedirectResponse(url='/docs', status_code=302)

# Register the routers
app.include_router(root_router)
app.include_router(api_router, prefix=settings.API_V1_PREFIX)