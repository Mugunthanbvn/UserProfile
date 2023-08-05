from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import UploadFile

from schemas import users as Schema
from db.models import users as Model
from db.utils import createHashedPassword
from db.db_connector import mongoDb



async def uploadUserProfile(uid: str,  image: UploadFile):
    imageData = await image.read()
    mongoDb['userProfile'].insert_one({'_id': uid, 'image': imageData, 'contentType': image.content_type})
    
async def createUser(db: Session, payload: Schema.CreateUser):
    userPayload  = payload.dict()
    userPayload['password'] = createHashedPassword(password=payload.password)
    image = userPayload.pop('image')
    user  = Model.User(**userPayload)
    db.add(user)
    db.commit()
    db.refresh(user)
    await uploadUserProfile(user.id, image)
    
def getProfile(userIds: List[int]):
    data = mongoDb['userProfile'].find( { '_id': {'$in': userIds}})
    return data or []

def getUser(db: Session, email: str, phone: Optional[str] = None) -> Schema.User:
    filters = [Model.User.email == email]
    if(phone):
        filters.append(Model.User.phone == phone)
    return db.query(Model.User).filter(*filters).first()

def getUserById(db: Session, id: int) -> Schema.User:
    return db.query(Model.User).filter(Model.User.id == id).first()

def getAllUsers(db: Session) -> list[Schema.User]:
    return db.query(Model.User).all()