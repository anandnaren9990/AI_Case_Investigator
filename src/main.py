from fastapi import FastAPI
from src.api.case import router as case_router
from src.api.alert_explanation import router as alert_explain_router

app = FastAPI()

app.include_router(case_router)
app.include_router(alert_explain_router)