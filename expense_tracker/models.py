from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    name: str
    surname: str
    age: int
    email: EmailStr


class UserNotFound(BaseModel):
    message: str = "Error: User Not Found"
    detail: int
