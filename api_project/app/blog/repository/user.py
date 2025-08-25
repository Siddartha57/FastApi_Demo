from api_project.blog import models
from api_project.blog import hashing
from fastapi import HTTPException,status

Hash = hashing.Hash

def create(db,request):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db):
    users = db.query(models.User).all()
    return users

def get_user(db,id):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    return user

def delete(db,id):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')
    user.delete(synchronize_session=False)
    db.commit()

    return {'details':f'user with id: {id} deleted sucessfully'}
