from typing import Dict, Any
import numpy as np

def meta():
    return {
        "title": "Matrix Inverse",
        "description": "Compute matrix inverse. Input as list of lists.",
        "inputs": {
            "matrix": {"type": "array", "required": True, "example": [[1,2],[3,4]]}
        }
    }

def execute(inputs: Dict[str, Any]) -> Dict[str, Any]:
    mat = inputs.get("matrix")
    try:
        a = np.array(mat, dtype=float)
        if a.ndim != 2 or a.shape[0] != a.shape[1]:
            return {"error": "Matrix must be square NxN."}
        inv = np.linalg.inv(a)
        return {"inverse": inv.tolist()}
    except Exception as e:
        return {"error": str(e)}
