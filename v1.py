from fastapi import APIRouter
from .calculators_router import router as calculators_router

router = APIRouter()
router.include_router(calculators_router, prefix="/calculator", tags=["calculator"])
