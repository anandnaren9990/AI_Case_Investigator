from fastapi import FastAPI
from src.api.case import router as case_router

app = FastAPI()

app.include_router(case_router)