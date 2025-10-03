from fastapi import APIRouter, HTTPException
from ..calculators import __all_modules__, load_module, module_metadata
from ..schemas.calculator_schemas import ExecRequest, ExecResponse

router = APIRouter()

@router.get("/modules")
async def list_modules():
    return {"modules": module_metadata()}

@router.post("/{module}/exec", response_model=ExecResponse)
async def exec_module(module: str, payload: ExecRequest):
    if module not in __all_modules__:
        raise HTTPException(status_code=404, detail="Calculator module not found")
    mod = load_module(module)
    result = mod.execute(payload.inputs)
    return {"module": module, "result": result, "meta": mod.meta()}
