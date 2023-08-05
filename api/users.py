from typing import List
from fastapi import Depends, APIRouter, HTTPException, Query
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pydantic import EmailStr
import base64


from db.crud import users as crud
from db.utils import getDb
from schemas.users import CreateUser, User, UserProfileResponse

router = APIRouter(
    prefix="/user",
    tags=["users"],
)

@router.get("/by-id/{id}", response_model=User)
def getUser(id: int, db: Session = Depends(getDb)):
    user = crud.getUserById(db = db, id=id)
    if(not user):
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/all", response_model=list[User])
def getUser( db: Session = Depends(getDb)):
    return crud.getAllUsers(db = db)

@router.post("/")
async def createUser( payload: CreateUser =   Depends(), db: Session = Depends(getDb)):
    try:
        user = crud.getUser(db = db, email=payload.email, phone=payload.phone)
        if(not user):
            await crud.createUser(db = db, payload=payload)
        else:
            raise HTTPException(status_code=500, detail='User already exists')
    except Exception as e:
        print(e)
        if(type(e) == HTTPException):
             raise e
        raise HTTPException(status_code=500, detail=f"User creation failed")
    return 'User created successfully'

@router.get("/profile", response_model=List[UserProfileResponse])
def getUserProfile(userIds: List[int] =  Query(...)):
    
    
    return list(map(lambda u: UserProfileResponse(id= u['_id'], contentType= u['contentType'], imageData= base64.b64encode(u['image'])), crud.getProfile(userIds=userIds)))

@router.get("/{email}", response_model=User)
def getUser(email: EmailStr, db: Session = Depends(getDb)):
    user = crud.getUser(db = db, email=email)
    if(not user):
        raise HTTPException(status_code=404, detail="User not found")
    return user



