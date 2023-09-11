from typing import Optional
from pydantic import BaseModel


class PersonBase(BaseModel):
    id: Optional[int]
    name: str
    phone: str

    class Config:
        orm_mode = True

class PersonUpdate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class Answer(BaseModel):
    message: str