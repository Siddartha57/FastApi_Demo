from fastapi import APIRouter,Depends,status
from api_project.blog import schemas, database
from sqlalchemy.orm import Session
from typing import List
from api_project.blog.repository import user

router = APIRouter(
    tags=['User'],
    prefix='/user'
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User, db:Session=Depends(get_db)):
    return user.create(db,request)

@router.get('/', response_model=List[schemas.ShowUser])
def get_users(db:Session=Depends(get_db)):
    return user.get_all(db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db:Session=Depends(get_db)):
    return user.get_user(db,id)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db:Session=Depends(get_db)):

    return user.delete(db,id)
