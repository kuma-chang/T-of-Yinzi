from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from .routes import router as UsersRouter


# Define models
class User(BaseModel):
    _id: int
    name: str
    description: Optional[str] = None



app = FastAPI()


@app.get("/")
async def root():
        return {"message": "Hello World"}


app.include_router(UsersRouter, prefix="/users")


"""
@app.post("/users/{user_name}")
async def add_user(user_name):
    routes.add_user(user_name)
    return{}
"""
