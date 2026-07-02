from datetime import datetime

from pydantic import BaseModel

from src.account.constans import UserSexEnum


class UserCreateSchema(BaseModel):
    fullname: str
    email: str
    sex: UserSexEnum

class UserResponseSchema(BaseModel):
    id: int
    name: str | None = None
    fullname: str
    age: int | None = None
    sex: UserSexEnum
    email: str
    created_at: datetime
    updated_at: datetime

class UserUpdateSchema(BaseModel):
    fullname: str
    email: str
    sex: UserSexEnum