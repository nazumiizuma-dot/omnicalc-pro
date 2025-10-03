from typing import Dict, Any
from scipy import integrate
from sympy import sympify, Symbol

def meta():
    return {
        "title": "Numeric Integral",
        "description": "Numeric integrate f(x) from a to b using quad",
        "inputs": {
            "expr": {"type": "string", "required": True, "example": "sin(x)"},
            "a": {"type": "number", "required": True, "example": 0},
            "b": {"type": "number", "required": True, "example": 3.1415}
        }
    }

def _make_func(expr_text: str):
    x = Symbol('x')
    expr = sympify(expr_text, evaluate=False)
    f = lambda val: float(expr.evalf(subs={x: val}))
    return f

def execute(inputs: Dict[str, Any]) -> Dict[str, Any]:
    expr = inputs.get("expr", "")
    a = float(inputs.get("a", 0))
    b = float(inputs.get("b", 1))
    try:
        f = _make_func(expr)
        val, err = integrate.quad(f, a, b, limit=100)
        return {"value": val, "error_estimate": err}
    except Exception as e:
        return {"error": str(e)}
