from fastapi import APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os


load_dotenv()
ATLAS_URI = os.environ.get('ATLAS_URI')

router = APIRouter()



@router.get("/")
async def get_all_users() -> dict:
    db = AsyncIOMotorClient(ATLAS_URI)
    all_users = await db["t-of-yinzi"]["test"].find().to_list(1000)
    db.close()
    return all_users


