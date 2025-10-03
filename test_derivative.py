from app.calculators import load_module
def test_derivative_simple():
    mod = load_module("derivative")
    r = mod.execute({"expr":"x**2"})
    assert "derivative" in r
    assert "2*x" in r["derivative"]
