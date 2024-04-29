from fastapi import FastAPI
from app.api import endpoints

app = FastAPI()

# Include API endpoints
app.include_router(endpoints.router)
