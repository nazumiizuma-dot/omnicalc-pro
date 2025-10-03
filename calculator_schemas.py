from pydantic import BaseModel
from typing import Any, Dict

class ExecRequest(BaseModel):
    inputs: Dict[str, Any]

class ExecResponse(BaseModel):
    module: str
    result: Dict[str, Any]
    meta: Dict[str, Any]
