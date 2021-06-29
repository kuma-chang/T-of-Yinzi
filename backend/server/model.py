from pydantic import BaseModel
from typing import Optional

# Define models
class User(BaseModel):
    _id: int
    name: str
    isTeacher: bool
    description: Optional[str] = None



