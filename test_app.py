from app import soma

def test_soma():
    assert soma(2,3) == 8

def test_soma_negativos():
    assert soma(-1, -1) == -2
