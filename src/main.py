from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings
app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    settings = get_settings()
    app.mongodb_client = AsyncIOMotorClient(settings.MONGODB_URI)
    app.db_client = app.mongodb_client[settings.MONGODB_DATABASE]
    
    yield  
    
    app.mongodb_client.close()    

app.include_router(base.base_router)
app.include_router(data.data_router)


