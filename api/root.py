""" Home page for API """

# Idée c'est de regrouper les endpoints par API

from fastapi import APIRouter
home_page = APIRouter(prefix='', tags=['home page'])

@home_page.get("/")
async def read_root() -> dict: 
    "Root endpoint for the API"
    return {"message": "Welcome to the FastAPI MLFLOW application made by Adam"}