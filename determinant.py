from typing import Dict, Any
import numpy as np

def meta():
    return {
        "title": "Determinant",
        "description": "Compute determinant of square matrix.",
        "inputs": {
            "matrix": {"type": "array", "required": True, "example": [[1,2],[3,4]]}
        }
    }

def execute(inputs: Dict[str, Any]) -> Dict[str, Any]:
    try:
        a = np.array(inputs.get("matrix"), dtype=float)
        det = float(np.linalg.det(a))
        return {"determinant": det}
    except Exception as e:
        return {"error": str(e)}
