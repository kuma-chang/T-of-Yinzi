from fastapi import APIRouter
import motor.motor_asyncio
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
ATLAS_URI = os.environ.get('ATLAS_URI')


router = APIRouter()



client = motor.motor_asyncio.AsyncIOMotorClient(ATLAS_URI)
db = client["t-of-yinzi"]
collection = db["test"]

@router.get("/")
async def get_all_users() -> dict:
    print(os.environ)
    all_users = await collection.find().to_list(1000)
    return all_users
loop = asyncio.get_event_loop()
loop.run_until_complete(get_all_users())
