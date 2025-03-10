from fastapi import FastAPI
from config.database import engine,Base
from app.cibc.user_bdl import user_bdl_route
from fastapi.middleware.cors import CORSMiddleware
import uvicorn 
from app.models.configuration import EmailSchema

from fastapi_pagination import Page, add_pagination, paginate
app=FastAPI()



origins = ["*"]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def welcome():
    return "Welcome to LW Intranet Portal Service"


app.include_router(user_bdl_route.router)

add_pagination(app)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level="info", reload = True)
    print("running")

