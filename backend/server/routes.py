from fastapi import APIRouter
import motor.motor_asyncio
from .config import ATLAS_URI
#from .server import get_all_users



router = APIRouter()


client = motor.motor_asyncio.AsyncIOMotorClient(ATLAS_URI)
db = client["t-of-yinzi"]
collection = db["test"]

@router.get("/")
async def get_all_users() -> dict:
    all_users = await collection.find().to_list(1000)
    return all_users
