from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from .model import UserModel
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


@router.get("/count")
async def get_all_users_count() -> dict:
    db = AsyncIOMotorClient(ATLAS_URI)
    users_count = await db["t-of-yinzi"]["test"].count_documents({})
    db.close()
    return users_count

@router.post("/add", response_description="Add new user", response_model=UserModel)
async def add_user(user: UserModel = Body(...)):
    user = jsonable_encoder(user)
    db = AsyncIOMotorClient(ATLAS_URI)
    new_user = await db["t-of-yinzi"]["test"].insert_one(user)
    created_user = await db["t-of-yinzi"]["test"].find_one({"id": new_user.inserted_id})
    db.close()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)





