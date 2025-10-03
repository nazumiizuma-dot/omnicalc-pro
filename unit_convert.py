from typing import Dict, Any

_CONVERSIONS = {
    ("m", "cm"): lambda v: v * 100,
    ("cm", "m"): lambda v: v / 100,
    ("kg", "g"): lambda v: v * 1000,
    ("g", "kg"): lambda v: v / 1000,
    ("m/s", "km/h"): lambda v: v * 3.6,
    ("km/h", "m/s"): lambda v: v / 3.6,
}

def meta():
    return {
        "title": "Unit Conversion",
        "description": "Simple unit conversions (expandable)",
        "inputs": {
            "value": {"type": "number", "required": True},
            "from": {"type": "string", "required": True},
            "to": {"type": "string", "required": True}
        }
    }

def execute(inputs):
    v = float(inputs.get("value", 0))
    fr = inputs.get("from")
    to = inputs.get("to")
    key = (fr, to)
    fn = _CONVERSIONS.get(key)
    if not fn:
        return {"error": f"Conversion {fr} -> {to} not supported"}
    return {"value": fn(v)}
