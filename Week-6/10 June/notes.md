# Pytest Examples

```python
# Calculator/calculator.py

def addition(num1: int, num2: int):
    return num1 + num2


def subtraction(num1: int, num2: int):
    return num1 - num2


def multiplication(num1: int, num2: int):
    return num1 * num2


def division(num1: int, num2: int):
    return num1 / num2


def main():
    while True:
        print("Welcome to the arithmetic calculator!")
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operation = input("Enter the operation you want to perform (+, -, *, /): ")
        if operation == '+':
            print(addition(num1, num2))
        elif operation == '-':
            print(subtraction(num1, num2))
        elif operation == '*':
            print(multiplication(num1, num2))
        elif operation == '/':
            print(division(num1, num2))
        else:
            print("Invalid operation")
            break


if __name__ == '__main__':
    main()

```

```python
# Calculator/test_arithmetic_calculator.py

import pytest
from calculator import addition, subtraction, multiplication, division


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

```

```shell
../Calculator> pytest

=========================================================================================== test session starts ============================================================================================
platform win32 -- Python 3.12.3, pytest-8.2.2, pluggy-1.5.0
rootdir: ..\Calculator
collected 4 items                                                                                                                                                                                           

test_arithmetic_calculator.py ....                                                                                                                                                                    [100%]

============================================================================================ 4 passed in 0.02s =============================================================================================

..\Calculator>pytest test_arithmetic_calculator.py::test_division
=========================================================================================== test session starts ============================================================================================ 
platform win32 -- Python 3.12.3, pytest-8.2.2, pluggy-1.5.0
rootdir: ..\Calculator
collected 1 item                                                                                                                                                                                             

test_arithmetic_calculator.py .                                                                                                                                                                       [100%] 

============================================================================================ 1 passed in 0.02s ============================================================================================= 
```
To run the python test markers
```commandline
pytest -m 
```

To stop test execution after first failure
```commandline
pytest -x
```

To stop after `n` number of failures
```commandline
pytest --maxfail=n
```