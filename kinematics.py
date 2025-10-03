from typing import Dict, Any
import math

def meta():
    return {
        "title": "Projectile Range (flat ground)",
        "description": "Compute range and max height for projectile launched at angle (neglecting air resistance).",
        "inputs": {
            "v0": {"type": "number", "required": True, "example": 20},
            "angle_deg": {"type": "number", "required": True, "example": 45},
            "g": {"type": "number", "required": False, "example": 9.81}
        }
    }

def execute(inputs):
    v0 = float(inputs.get("v0", 0))
    angle = math.radians(float(inputs.get("angle_deg", 45)))
    g = float(inputs.get("g", 9.81))
    range_ = (v0**2) * math.sin(2*angle) / g
    hmax = (v0**2) * (math.sin(angle)**2) / (2*g)
    t_flight = 2 * v0 * math.sin(angle) / g
    return {"range": range_, "max_height": hmax, "time_of_flight": t_flight}
