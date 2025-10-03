from app.calculators import load_module
def test_matrix_inverse_identity():
    mod = load_module("matrix_inverse")
    r = mod.execute({"matrix": [[1,0],[0,1]]})
    assert "inverse" in r
    assert r["inverse"] == [[1.0,0.0],[0.0,1.0]]
