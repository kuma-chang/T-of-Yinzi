from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import server 


# Define models
class User(BaseModel):
    _id: int
    name: str
    description: Optional[str] = None



app = FastAPI()


@app.get("/")
async def root():
        return {"message": "Hello World"}

@app.get("/users")
async def get_all_users():
    all_users = server.get_all_users()
    return all_users


@app.post("/users/{user_name}")
async def add_user(user_name):
    server.add_user(user_name)
    return{}
