from typing import Dict, Any
import numpy as np

def meta():
    return {
        "title": "Basic Statistics",
        "description": "Compute mean, median, std for a list of numbers",
        "inputs": {
            "data": {"type": "array", "required": True, "example": [1,2,3,4,5]}
        }
    }

def execute(inputs):
    arr = np.array(inputs.get("data", []), dtype=float)
    if arr.size == 0:
        return {"error": "Empty data"}
    return {"mean": float(arr.mean()), "median": float(np.median(arr)), "std": float(arr.std(ddof=0))}
