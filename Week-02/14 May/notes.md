# Python Functions

## Introduction

Functions are blocks of code that perform a specific task, and they allow us to break down our programs into smaller,
manageable pieces. In Python, functions are defined using the `def` keyword, followed by the function name and
parameters in parentheses.

## Defining a Function

```python
def greet(name):
    print("Hello, " + name + "!")
```

## Calling a Function

To call a function, simply write its name followed by parentheses, passing any required arguments inside the
parentheses.

```python
greet("Alice")
```

## Parameters and Arguments

Parameters are variables that are defined in the function signature, while arguments are the actual values passed to the
function when it's called.

```python
def add(x, y):
    return x + y

result = add(3, 5)
print(result)  # Output: 8
```

## Return Statement

Functions can return values using the `return` statement. If no return statement is specified, the function
returns `None` by default.

```python
def square(x):
    return x * x

result = square(4)
print(result)  # Output: 16
```

## Default Parameters

Default parameter values can be specified in the function definition. These default values are used if the function is
called without providing a corresponding argument.

```python
def greet(name="World"):
    print("Hello, " + name + "!")

greet()        # Output: Hello, World!
greet("Alice") # Output: Hello, Alice!
```

## Variable Number of Arguments

Python allows functions to accept a variable number of arguments using the `*args` and `**kwargs` syntax.

```python
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))  # Output: 24
```

## Lambda Functions

Lambda functions, also known as anonymous functions, are small, inline functions that can have any number of arguments
but only one expression.

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

## Scope of Variables

Variables defined inside a function are local to that function by default. However, Python allows access to global
variables within functions using the `global` keyword.

```python
x = 10

def func():
    global x
    x += 5
    print(x)

func()  # Output: 15
```

## Recursion

Recursion is a technique in which a function calls itself to solve smaller instances of the same problem. It's important
to have a base case to prevent infinite recursion.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
```

## Docstrings

Docstrings are string literals enclosed in triple quotes that appear as the first statement in a function, module,
class, or method definition. They are used to provide documentation about the object they precede.

```python
def greet(name):
    """
    This function greets the person with the given name.
    """
    print("Hello, " + name + "!")
```

Ah, I see! You're referring to passing functions as arguments or returning them from other functions. Here's how you can
do that in Python:

# Python Functions

## Introduction

Functions are first-class citizens in Python, which means they can be treated like any other object, including passing
them as arguments to other functions or returning them from other functions.

## Defining Functions

```python
def greet(name):
    return "Hello, " + name + "!"
```

## Passing Functions as Arguments

Functions can be passed as arguments to other functions, allowing for flexible and dynamic behavior.

```python
def call_function(func, arg):
    return func(arg)

result = call_function(greet, "Alice")
print(result)  # Output: Hello, Alice!
```

## Returning Functions

Functions can also be returned from other functions, enabling higher-order functions.

```python
def get_greeting_function():
    def greet(name):
        return "Hello, " + name + "!"
    return greet

greet_function = get_greeting_function()
result = greet_function("Bob")
print(result)  # Output: Hello, Bob!
```
