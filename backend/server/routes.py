from fastapi import APIRouter, Depends
from .mongodb import AsyncIOMotorClient, get_database
import os


router = APIRouter()



@router.get("/")
async def get_all_users(
        db: AsyncIOMotorClient = Depends(get_database)
        ) -> dict:
    print(db)
    all_users = await db["t-of-yinzi"]["test"].find().to_list(1000)
    return all_users


