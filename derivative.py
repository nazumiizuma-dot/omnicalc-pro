from typing import Dict, Any
from sympy import sympify, diff, Symbol

def meta():
    return {
        "title": "Symbolic Derivative",
        "description": "Compute d/dx of an expression. variable optional default 'x'",
        "inputs": {
            "expr": {"type": "string", "required": True, "example": "sin(x) * x**2"},
            "var": {"type": "string", "required": False, "example": "x"}
        }
    }

def execute(inputs: Dict[str, Any]) -> Dict[str, Any]:
    expr_text = inputs.get("expr", "")
    var = inputs.get("var", "x")
    try:
        x = Symbol(var)
        expr = sympify(expr_text, evaluate=False)
        derivative = diff(expr, x)
        return {"derivative": str(derivative), "steps": [f"d/d{var}({expr_text}) = {derivative}"]}
    except Exception as e:
        return {"error": str(e)}
