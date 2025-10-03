from typing import Dict, Any
import math

def meta():
    return {
        "title": "Quadratic Equation",
        "description": "Solve ax^2 + bx + c = 0 (real roots)",
        "inputs": {
            "a": {"type": "number", "required": True, "example": 1},
            "b": {"type": "number", "required": True, "example": 0},
            "c": {"type": "number", "required": True, "example": -4}
        }
    }

def execute(inputs: Dict[str, Any]) -> Dict[str, Any]:
    a = float(inputs.get("a", 0))
    b = float(inputs.get("b", 0))
    c = float(inputs.get("c", 0))
    if a == 0:
        return {"error": "Coefficient a cannot be zero for quadratic equation."}
    disc = b*b - 4*a*c
    if disc < 0:
        root1 = complex(-b, math.sqrt(-disc)) / (2*a)
        root2 = complex(-b, -math.sqrt(-disc)) / (2*a)
    else:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
    steps = [
        f"Discriminant = b^2 - 4ac = {disc}",
        f"Root1 = (-b + sqrt(D))/2a = {root1}",
        f"Root2 = (-b - sqrt(D))/2a = {root2}"
    ]
    return {"roots": [root1, root2], "discriminant": disc, "steps": steps}
