from typing import Dict, Any
import numpy as np

def meta():
    return {
        "title": "Solve Linear System",
        "description": "Solve Ax = b where A is NxN and b is vector",
        "inputs": {
            "A": {"type": "array", "required": True, "example": [[3,2],[1,2]]},
            "b": {"type": "array", "required": True, "example": [5,5]}
        }
    }

def execute(inputs):
    try:
        A = np.array(inputs.get("A"), dtype=float)
        b = np.array(inputs.get("b"), dtype=float)
        x = np.linalg.solve(A, b)
        return {"solution": x.tolist()}
    except Exception as e:
        return {"error": str(e)}
