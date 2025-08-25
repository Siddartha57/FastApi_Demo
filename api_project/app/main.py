from fastapi import FastAPI, Depends, status, HTTPException
from blog import schemas,models
from blog.database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import List
from blog.hashing import Hash
from blog.routers import blog,user,authenticate

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authenticate.router)




