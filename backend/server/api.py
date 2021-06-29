from fastapi import FastAPI
from .users import router as UsersRouter



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
