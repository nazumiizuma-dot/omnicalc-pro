from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1 import router as api_router
from .config import settings
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

app = FastAPI(title="OmniCalc Pro API", version="0.1.0", openapi_url="/api/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/healthz")
async def health():
    return {"status": "ok"}
