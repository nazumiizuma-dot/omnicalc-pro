from typing import Dict, Any

class CalculatorBase:
    @staticmethod
    def meta() -> Dict[str, Any]:
        raise NotImplementedError

    @staticmethod
    def execute(inputs: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError
