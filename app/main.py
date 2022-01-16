# Python
import os, sys
from uuid import uuid4

# FastAPI
from fastapi import FastAPI, Depends, Body, Query, Path

from fastapi_pagination import Page, Params, paginate

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

@app.get("/api/properties", response_model=Page[SchemaProperty])
def get_properties(params: Params = Depends()):
    properties = db.session.query(ModelProperty).all()
    return paginate(properties, params)

@app.post("/api/properties", response_model=SchemaProperty)
def create_property(property: SchemaProperty):
    db_property = ModelProperty(
        bed = property.bed,
        bath = property.bath,
        parking_spots = property.parking_spots,
        size = property.size,
        price = property.price,
        type = property.type.value
    )
    db.session.add(db_property)
    db.session.commit()
    return db_property