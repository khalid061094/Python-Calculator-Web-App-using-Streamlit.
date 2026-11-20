from calculator import calculate

def test_addition():
    assert calculate(10, 5, "Addition (+)") == 15

def test_subtraction():
    assert calculate(10, 5, "Subtraction (-)") == 5

def test_multiplication():
    assert calculate(10, 5, "Multiplication (*)") == 50

def test_division():
    assert calculate(10, 5, "Division (/)") == 2

def test_modulus():
    assert calculate(10, 3, "Modulus (%)") == 1

def test_division_by_zero():
    try:
        calculate(10, 0, "Division (/)")
        assert False, "Expected ValueError"
    except ValueError:
        assert True

def test_invalid_operation():
    try:
        calculate(10, 5, "Power")
        assert False, "Expected ValueError"
    except ValueError:
        assert True
