# Functions in Python
## Types of Functions in Python
- **Predefined**
- **User Defined**

## Python Function Arguments
- **Positional Arguments**
  - In these types of functions we need to pass arguments in the same sequence and in the same amount 
```python
def show_msg(name, i_d):
    print("Hello: ", name)
    print("Your Id is: ", i_d)

if __name__ == '__main__':
    show_msg("aayush", 7)
    show_msg(7,"aayush")
```
```commandline
Hello:  aayush
Your Id is:  7
Hello:  7
Your Id is:  aayush
```
- **Keyword Argument**
  - In this type of functions we can pass the arguments in any order but not more than what is required
```python
def show_msg(name, i_d):
    print("Hello: ", name)
    print("Your Id is: ", i_d)

if __name__ == '__main__':
    show_msg(name="aayush", i_d=7)
    show_msg(i_d=7, name="aayush")

```
```commandline
Hello:  aayush
Your Id is:  7
Hello:  aayush
Your Id is:  7

```
- **Mixed functions with both positional and keyword arguments**
  - In this type of function we need to give the keyword arguments after the positional arguments always
```python
def show_msg(name, i_d):
    print("Hello: ", name)
    print("Your Id is: ", i_d)

if __name__ == '__main__':
    show_msg(7, i_d="aayush")
```
```commandline
Hello:  7
Your Id is:  aayush

```
- **Defaut Arguments**
  - They are already assigned with default values
```python
def show_msg(num1=0, num2=0):
    print(f"value of num1 = {num1} and the value of num 2 = {num2}")
if __name__ == '__main__':
    show_msg(10)
    show_msg(10,20)
    show_msg(10,20,30,40,)
```
```commandline
Traceback (most recent call last):
  File "D:\Python Training\15 May\Prods\Class Codes\demo_funcs.py", line 6, in <module>
    show_msg(10,20,30,40,)
TypeError: show_msg() takes from 0 to 2 positional arguments but 4 were given
value of num1 = 10 and the value of num 2 = 0
value of num1 = 10 and the value of num 2 = 20
```
- **Variable Length Argumnets in Functions**
  - This is used to incorporate multiple arguments in the function
```python
def show_msg(*num):
    num = list(num)
    for n in num:
        print(f"value of num {n}")
if __name__ == '__main__':
    show_msg(10)
    show_msg(10,20)
    show_msg(10,20,30,40,)

```
```commandline
value of num 10
value of num 10
value of num 20
value of num 10
value of num 20
value of num 30
value of num 40
```
```python
def show_msg(num1, *num):
    print(num1)
    num = list(num)
    for n in num:
        print(f"value of num {n}")
if __name__ == '__main__':
    show_msg(10)
    show_msg(10,20)
    show_msg(10,20,30,40,)
```
```commandline
10
10
value of num 20
10
value of num 20
value of num 30
value of num 40
```
```python
def show_msg(*num, num1):
    print(num1)
    num = list(num)
    for n in num:
        print(f"value of num {n}")
if __name__ == '__main__':
    show_msg(10)
    show_msg(10,20)
    show_msg(10,20,30,40,)
```
```commandline
Traceback (most recent call last):
  File "D:\Python Training\15 May\Prods\Class Codes\demo_funcs.py", line 7, in <module>
    show_msg(10)
TypeError: show_msg() missing 1 required keyword-only argument: 'num1'
```
To resolve this we need to give num1 always as keyword argument
```python
def show_msg(*num, num1):
    print(num1)
    num = list(num)
    for n in num:
        print(f"value of num {n}")
if __name__ == '__main__':
    show_msg(num1=10)
    show_msg(10,num1=20)
    show_msg(10,20,30,num1=40,)

```
```commandline
10
20
value of num 10
40
value of num 10
value of num 20
value of num 30
```
## Recursive Python Functions
```python
def show(x):
    if x < 10:
        show(x + 1)
    print(x)


if __name__ == '__main__':
    show(1)

```
```commandline
10
9
8
7
6
5
4
3
2
1
```
## Anonymous Functions
```python
if __name__ == '__main__':
    num1 = 10
    num2 = 20
    print(f"The biggest number between {num1} and {num2} is {(lambda num1, num2: num1 if num1 > num2 else num2)(num1, num2)}")

```
```commandline
The biggest number between 10 and 20 is 20
```

## Filter Function
```python
def iseven(x):
    if x['exp'] >= 3:
        return True
    else:
        return False


if __name__ == '__main__':
    l = [{'name': 'aayush3', 'exp': 3}, {'name': 'aayush2', 'exp': 2}, {'name': 'aayush1', 'exp': 1},
         {'name': 'aayush7', 'exp': 7}]
    l1 = list(filter(iseven, l))
    print(l1)
```
```commandline
[{'name': 'aayush3', 'exp': 3}, {'name': 'aayush7', 'exp': 7}]
```
Using Anonymous Functions
```python
def iseven(x):
    if x['exp'] >= 3:
        return True
    else:
        return False


if __name__ == '__main__':
    l = [{'name': 'aayush3', 'exp': 3}, {'name': 'aayush2', 'exp': 2}, {'name': 'aayush1', 'exp': 1},
         {'name': 'aayush7', 'exp': 7}]
    # l1 = list(filter(iseven, l))
    l1 = list(filter(lambda x : True if x['exp'] >= 3 else False, l))
    print(l1)

```
```commandline
[{'name': 'aayush3', 'exp': 3}, {'name': 'aayush7', 'exp': 7}]

```

## Map Function
```python
if __name__ == '__main__':
    numbers = (1, 2, 3, 4)
    result = map(lambda x: x + x, numbers)
    print(list(result))
```
```commandline
[2, 4, 6, 8]
```

## Reduce Functions
```python
from functools import reduce


def product(x, y):
    print('Value: ', x, y)
    return x * y


if __name__ == '__main__':
    ans = reduce(product, [2, 5, 3, 7])
    print(ans)

```
```commandline
Value:  2 5
Value:  10 3
Value:  30 7
210
```

## Nested Functions
```python
def outer_function(text):
    text = text

    def inner_function():
        print("Inner Function")
        print(text)

    print("Outer Function")
    inner_function()


if __name__ == '__main__':
    outer_function('Hey !')

```
```commandline
Outer Function
Inner Function
Hey !
```

```python
def outer_function():
    print("Outer Function")

    def inner_function():
        print("Inner Function")

    return inner_function


if __name__ == '__main__':
    func = outer_function()()

```
```commandline
Outer Function
Inner Function
```
# Scope of a Variable
- ## Global Variable
- ## Local Variable
```python
global num
num = 100


def fun1():
    print(num)


def fun2():
    num = 400
    print(num)


def fun3():
    global num
    num = 200
    print(num)


def fun4():
    print(num)


if __name__ == '__main__':
    fun1()
    fun2()
    fun3()
    fun4()

```

```commandline
100
400
200
200
```
