from fastapi import FastAPI, Depends, status, HTTPException
from api_project.app.blog import schemas, models
from api_project.app.blog import database
from api_project.app.blog.database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from api_project.app.blog.hashing import Hash
from api_project.app.blog.routers import blog, user, authenticate

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authenticate.router)






