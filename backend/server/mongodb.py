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
    print("connecting to Mongo")
    db.client = AsyncIOMotorClient(ATLAS_URI)
    print("connected to Mongo successfully!")

async def close_mongo_connection():
    print("closing Mongo connection")
    db.client.close()
    print("closed Mongo connection successfully!")
