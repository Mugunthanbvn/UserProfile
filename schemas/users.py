import base64
from typing import Optional
from pydantic import BaseModel, EmailStr
from fastapi import UploadFile, File

class UserProfile(BaseModel):
    image: UploadFile
    
class UserProfileResponse(BaseModel):
    id: int
    imageData: str
    contentType: str


class UserInfo(BaseModel):
    firstname: str
    lastname: str
    phone: str
    email: EmailStr
    
class User(UserInfo):
    id: int
    class Config:
        orm_mode = True

class CreateUser(UserInfo, UserProfile):
    password: str

