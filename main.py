# FastAPI
from fastapi import FastAPI, Body, Query, Path

app = FastAPI()


@app.get("/")
def home():
    return {"message": "hello world"}