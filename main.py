from fastapi import FastAPI, Depends
from app import models
from app.db import engine
from app.db import SessionLocal
from app import crud
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)
#initailize FastApi instance
app = FastAPI()


#define endpoint
# @app.get("/")
# def home():
#     return {"name": "Jaswant"}
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#define endpoint
@app.post("/create_address")
def create_address(first_name:str, last_name:str, age:int, phone_no:str, email:str, ip:str, db:Session = Depends(get_db)):
    address = crud.create_address(db=db, first_name=first_name, last_name=last_name, age=age, phone_no=phone_no,email=email, ip = ip)
##return object created
    return {"address": address}

@app.get("/get_address/{ip}/{distance}/") #id is a path parameter
def get_address(ip:str, distance:int, db:Session = Depends(get_db)):
    """
    the path parameter for id should have the same name as the argument for id
    so that FastAPI will know that they refer to the same variable
Returns a address object if one with the given id exists, else null
    """
    address = crud.get_address(db=db, ip=ip,distance=distance )
    return address