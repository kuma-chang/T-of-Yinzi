from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
ATLAS_URI = os.environ.get('ATLAS_URI')

class Database:
    client: AsyncIOMotorClient = None

db = Database()

async def get_database() -> AsyncIOMotorClient:
    return db.client



async def connect_to_mongo():
    db.client = AsyncIOMotorClient(ATLAS_URI)

async def close_mongo_connection():
    db.client.close()
