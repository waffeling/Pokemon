from fastapi import FastAPI, Response, status, Request
from app.routers import imageapi
from app.routers import sqlapi


app = FastAPI()

app.include_router(imageapi.router)
app.include_router(sqlapi.router)
