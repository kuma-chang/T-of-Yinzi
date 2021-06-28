from fastapi import APIRouter, Depends
from .mongodb import AsyncIOMotorClient, get_database
import os


from dotenv import load_dotenv
load_dotenv()
ATLAS_URI = os.environ.get('ATLAS_URI')

router = APIRouter()



@router.get("/")
async def get_all_users() -> dict:
    db = AsyncIOMotorClient(ATLAS_URI)
    print(db)
    all_users = await db["t-of-yinzi"]["test"].find().to_list(1000)
    db.close()
    return all_users


'''
        db: AsyncIOMotorClient = Depends(get_database)

'''
