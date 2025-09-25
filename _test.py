import pytest

def square(n):
    return n**2

def cube(n):
    return n ** 3

def fifth_power(n):
    return n**5

def test_square():
    assert square(2)==4,"Test Failed"
    assert square(3)==9, "Test Failed"

def test_cube():
    assert cube(2) == 8, "Test Failed"
    assert cube(3) == 27, "Test Failed"

def test_fifth_power():
    assert fifth_power(2) == 32, "Test Failed"
    assert fifth_power(3) ==243, "Test Failed"


def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")