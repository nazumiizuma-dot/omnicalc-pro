from app.calculators import load_module
def test_quadratic_real_roots():
    mod = load_module("quadratic")
    r = mod.execute({"a":1,"b":0,"c":-4})
    roots = r.get("roots")
    assert len(roots)==2
    assert any(abs(rt - 2) < 1e-6 for rt in roots if isinstance(rt, (int,float)))
