from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
        example="example@example.com"
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Username123"
    )


class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )


class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="strongpass"
    )