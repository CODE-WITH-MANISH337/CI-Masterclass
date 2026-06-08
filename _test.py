import pytest

def square(n):
    return n**2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5

# Testing the square 
def test_square():
    assert square(2)==4, "Test Failed Square of 2 should be 4"
    assert square(3)==9, "Test Failed sqaure of 3 should be 9"

def test_cube():
    assert cube(2)==8 ,"Test Failed cube of 2 should be 8" 
    assert cube(3)==27,"Test Failed cube of 3 should be 27"


def test_fifth():
    assert fifth_power(2)==32,"Test failed fifth_power of 2 should be 32"
    assert fifth_power(3)==243,"Test failed fifth_power of 3 should be 243"

def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")