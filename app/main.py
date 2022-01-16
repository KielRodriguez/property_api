# Python
import os, sys
from uuid import uuid4

# FastAPI
from fastapi import FastAPI, Body, Query, Path

# SQLAlchemy
from fastapi_sqlalchemy import DBSessionMiddleware, db

from .models import Property as ModelProperty
from .schemas import Property as SchemaProperty
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get("/api/ping")
def home():
    return {"ping": "pong"}


@app.post("/api/property", response_model=SchemaProperty)
def create_property(property: SchemaProperty):
    print("======================")
    print(property)
    db_property = ModelProperty(
        bed = property.bed,
        bad = property.bad,
        parking_spots = property.parking_spots,
        size = property.size,
        price = property.price
    )
    db.session.add(db_property)
    db.session.commit()
    return db_property