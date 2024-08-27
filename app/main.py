from fastapi import FastAPI
from app.api.endpoints import feedback

app = FastAPI()

app.include_router(feedback.router)
