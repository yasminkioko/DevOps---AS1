from calculadora import operations

def test_sum():
    op = operations()
    assert op.sum(2, 1) == 3

def test_subtraction():
    op = operations()
    assert op.subtraction(3, 1) == 2

def test_multiplication():
    op = operations()
    assert op.multiplication(2, 3) == 6

def test_division():
    op = operations()
    assert op.division(4, 2) == 2
    assert op.division(4, 0) == None