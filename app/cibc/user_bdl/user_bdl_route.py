from fastapi import FastAPI, Depends, Form, HTTPException, Query, status
from sqlalchemy.orm import Session,load_only
from fastapi_pagination import Page, add_pagination, paginate, Params,LimitOffsetPage
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from typing import List, Optional
from starlette.responses import JSONResponse
from sqlalchemy import MetaData
from fastapi import APIRouter, Depends,Path,BackgroundTasks
from config.database import engine, Base
from app.models.configuration import EmailSchema
from app.dto.schemas import UserSchemas
from app.models.configuration import Usermodel
from config.database import SessionLocal
from app import models
from config.database import conn,conf
from fastapi_pagination import paginate, Page, Params
from sqlalchemy import select
from config.database import get_db
from sqlalchemy import desc,asc,or_
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
import smtplib



router = APIRouter(prefix="/User", tags=["User"])


# view user


@router.get("/user/get/{id}")
def read_user(id: int, name: str = None, db: Session = Depends(get_db)):
    user = db.query(Usermodel).filter(Usermodel.id == id).first()
    return {'user':user}


# get all user and search and pagination,sorting 
@router.get('/get_all_user', summary="Get all user")
def get_all_user(search:str,params: Params=Depends(),sort_by:str = None, sort_direction:str = None, db: Session = Depends(get_db)):#,params: Params = Depends(),
    fetch_user = db.query(Usermodel).options(load_only(Usermodel.id,Usermodel.name))
    print(fetch_user)
    if sort_direction=="desc":
        fetch_user=fetch_user.order_by(Usermodel.__dict__[sort_by].desc())
    elif sort_direction=="asc":     
        fetch_user=fetch_user.order_by(Usermodel.__dict__[sort_by].asc())
    else:
        fetch_user=fetch_user.order_by(Usermodel.id.desc())
    
    updated_all_user =fetch_user.all()
    
    if search:
        fetch_user = fetch_user.filter(or_(
             Usermodel.name.like('%'+search+'%'),
                Usermodel.email.like('%'+search+'%')
            ))

    return paginate(updated_all_user,params)    





    

# search user

@router.get("/searchuser")
def search_user(id,name):
    return {"id":id,"name":name}


 # create user
@router.post('/user')
def create(request:UserSchemas, db: Session = Depends(get_db)):
    new_user = Usermodel(id=request.id, name=request.name,email=request.email,password=request.password)
    db.add(new_user)
    db.refresh(new_user)
    print("sucessfully sent")
    print(new_user)
    db.refresh(new_user)
    db.commit()
    return new_user
    


# update user


@router.put("/user/update/{id}")
def update_user(id: int, request: UserSchemas, db: Session = Depends(get_db)):
    user = db.query(Usermodel).filter(Usermodel.id == id)
    if not user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"user {id} not found")
    user.update(request.dict())
    db.commit()
    return "update user with id {id}"


# delete user

@router.delete("/user/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    db.query(Usermodel).filter(Usermodel.id ==
                               id).delete(synchronize_session=False)
    return "delete user id with id {id}"



# SEND MAIL


'''def handle_email_background(email:str,data:str):
    print(email)
    print(data)

@router.get("/sendmail")
def  handle_email(email:str,background_task:BackgroundTasks):
    print(email)
    background_task.add_task(handle_email_background,email,"this is sample background")
    return {"user":"bardwaj","message":"mailsent"}
'''

# send mail

html = """
<p>Thanks for using Fastapi-mail</p> 
"""
@router.post("/emailsend")
def simple_send(email: str, background_task: BackgroundTasks)->JSONResponse:
    message = MessageSchema(
    subject="Fastapi-Mail module",
    recipients=[email],
    body=html,
    subtype=MessageType.html)
    fm = FastMail(conf)
    background_task.add_task(fm.send_message,message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})     




'''sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"'''
'''
message = f"""\
Subject: Hi Mailtrap
To: {"amita.dhandha@gmail.com"}
From: {"amita.verve@gmail.com"}

This is a test e-mail message."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("c2ba5ee6a4cea9", "105e726496cfc2")
    server.sendmail(sender, receiver, message)'''