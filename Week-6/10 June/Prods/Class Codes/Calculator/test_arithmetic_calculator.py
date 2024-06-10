import pytest
from calculator import addition, subtraction, multiplication, division, main


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-2, 3) == 1
    assert addition(-2, -3) == -5


def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(-5, 3) == -8
    assert subtraction(-5, -3) == -2


def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-2, 3) == -6
    assert multiplication(-2, -3) == 6


def test_division():
    assert division(6, 3) == 2
    assert division(-6, 3) == -2
    assert division(-6, -3) == 2
    with pytest.raises(ZeroDivisionError):
        division(6, 0)


