from sqlalchemy.orm import Session
from api_project.app.blog import models
from fastapi import HTTPException,status

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(db,request):
    new_blog = models.Blog(title=request.title,body=request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blog(db,id):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
    return blog

def update(db,id,request):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
    blog.update(request.dict())
    db.commit()
    return {'details':f'blog {id} updated sucessfully'}

def delete(db,id):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    blog.delete(synchronize_session=False)
    db.commit()

    return {'details':f'Blog with {id} deleted sucessfully'}

