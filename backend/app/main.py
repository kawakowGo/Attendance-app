import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.me import router as me_router

load_dotenv()
app=FastAPI(title=os.getenv("APP_NAME","Attendance App"))

app.include_router(me_router)

@app.get("/health")
def health():
    return{"status":"ok"}