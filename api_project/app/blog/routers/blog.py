from fastapi import APIRouter, Depends, status
from typing import List,Annotated
from api_project.app.blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from api_project.app.blog.repository import blog


router = APIRouter(
    tags=['Blog'],
    prefix='/blog'
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def get_all(db:Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog, db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(db,request)


@router.get('/{id}', response_model=schemas.ShowBlog)
def get_one(id: int,db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_blog(db,id)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request:schemas.Blog, db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(db,id,request)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):

    return blog.delete(db,id)

