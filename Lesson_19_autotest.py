#3.2 module
#1
def test_input_text(x, y):
    assert (x == y), f"expected {x}, got {y}"

------------
#2
def test_substring(x, y):
    assert y in x, f"expected '{y}' to be substring of '{x}'"