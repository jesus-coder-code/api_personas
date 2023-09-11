from fastapi import FastAPI
#from models.person import *
from routes.personRoute import *
from config.database import SessionLocal, engine
from models.person import *
from schemas.personSchema import *

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router)
