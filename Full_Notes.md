# Python: A Versatile and Widely Used Language

## Why Python is Popular?

- **General Purpose:**
  - Widely used across diverse domains such as web development, data science, artificial intelligence, and more.
- **Platform Independent:**
  - Python's code can run on any platform without modification, enhancing its portability.
  - Being an interpreted language, Python offers ease of debugging and faster development cycles.
- **Embeddable:**
  - Python is embeddable within applications written in other languages like C/C++, allowing for scripting capabilities
    and rapid prototyping.
- **Extensible:**
  - Python supports extending its functionality by integrating modules and libraries written in other languages like
    C/C++.

## Variable

- A variable serves as a named memory location to store values. Python variables do not require explicit declaration of
  data types, making the language more flexible and concise.

### Python's Dynamic Typing

- Python dynamically assigns data types to variables during execution, leading to more flexible coding and reduced
  development time.

# Immutable Data Types

- **Numbers:** Integers, floating-point numbers, and complex numbers are immutable data types in Python.
- **Strings:** Immutable sequences of characters that support various manipulation methods such as slicing,
  concatenation, and formatting.
- **Tuples:** Immutable ordered collections of elements, often used for grouping related data.
- **Frozen Sets:** Immutable collections of unique elements, similar to sets but with immutability.

# Type Casting

- Python supports type casting between compatible data types using functions like `int()`, `float()`, `str()`, etc.
- Conversion from complex to int is not supported due to the potential loss of precision.

### Unary Operations

- Python does not support unary operations directly; however, many unary operations can be achieved using built-in
  functions and operators.

## Additional Features of Python

- **High-level Language:** Python abstracts complex low-level details, enabling programmers to focus on solving problems
  efficiently.
- **Rich Standard Library:** Python comes with a vast standard library that provides modules and functions for various
  tasks, reducing the need for external dependencies.
- **Community Support:** Python has a large and active community of developers who contribute to its growth by creating
  libraries, frameworks, and documentation.
- **Readability:** Python emphasizes code readability and simplicity, making it easier to write, understand, and
  maintain code.
- **Interpreted and Compiled:** Python code is interpreted line-by-line, but it can also be compiled into bytecode for
  improved performance.
- **Object-Oriented:** Python supports object-oriented programming paradigms, facilitating the creation and management
  of complex software systems.

These comprehensive notes cover the fundamental aspects of Python's popularity, its core features, and additional
characteristics that make it a preferred choice for various applications.

# Strings in Python

## Introduction

Strings are one of the most fundamental data types in Python, representing sequences of characters. In Python,
everything is treated as an object, including strings. They are immutable, meaning they cannot be changed once created.
Here are some key points about strings:

- **Definition**: A string is a sequence of characters stored in contiguous memory locations.
- **Properties**:
  - **Ordered**: Strings maintain the order of characters, with each character having a unique position.
  - **Indexable**: Individual characters within a string can be accessed using numerical indices.
  - **Immutable**: Strings cannot be modified once created.
- **Representation**: Strings in Python are enclosed in single (`'`) or double (`"`) quotes.
- **Multiline Strings**: Python supports multiline strings using triple quotes (`'''` or `"""`).

## Handling Strings in Python

- **String Concatenation**:
  ```python
  str1 = "Hello"
  str2 = "World"
  result = str1 + " " + str2  # Output: "Hello World"
  ```

- **String Methods**:
  Python provides various built-in methods for string manipulation, such
  as `upper()`, `lower()`, `strip()`, `replace()`, `split()`, `join()`, etc.

- **String Formatting**:
  Python supports various string formatting techniques using the `%` operator, `format()` method, and f-strings.

- **String Slicing**:
  ```python
  my_string = "Python"
  print(my_string[1:4])  # Output: "yth"
  ```

## Applications of Strings in Python

- **Text Processing**: Used extensively in text editors, word processors, and data processing applications.
- **Pattern Matching**: Python's `re` module allows pattern matching using regular expressions.
- **Data Representation**: Strings are used to represent various types of data, including names, addresses, and textual
  information.
- **Data Compression**: String compression algorithms are employed to reduce storage requirements.

## Advantages of Strings in Python

- **Widely Supported**: Strings are fundamental in Python and are extensively supported across libraries and frameworks.
- **Efficient Manipulation**: Python provides efficient algorithms for string manipulation and processing.
- **Modeling Real-World Data**: Strings are versatile and can model a wide range of real-world textual data.

## Disadvantages of Strings in Python

- **Encoding Issues**: Strings can have different encodings (e.g., UTF-8, UTF-16), leading to compatibility issues.
- **Immutable**: Once created, strings cannot be modified directly, which can be limiting in certain scenarios.
- **Concatenation Performance**: String concatenation operations can be slow due to the creation of new string objects.

## Conclusion

Strings are essential in Python for representing and manipulating textual data. Understanding how to effectively handle
strings is crucial for developing robust and efficient Python applications.

# Python Lists

## Introduction

Lists are a versatile and fundamental data structure in Python used to store collections of items. They are ordered,
mutable (modifiable), and can contain elements of different data types. Lists are defined using square brackets `[ ]`
and elements are separated by commas.

## Creating Lists

```python
# Empty list
empty_list = []

# List with elements
my_list = [1, 2, 3, 4, 5]

# List with mixed data types
mixed_list = [1, 'hello', True, 3.14]
```

## Accessing Elements

Elements in a list can be accessed using indexing and slicing.

```python
my_list = [1, 2, 3, 4, 5]

# Accessing single element
print(my_list[0])  # Output: 1

# Slicing
print(my_list[1:4])  # Output: [2, 3, 4]
```

## Modifying Lists

Lists are mutable, meaning you can change their content.

```python
my_list = [1, 2, 3, 4, 5]

# Changing an element
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

# Appending elements
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Removing elements
my_list.remove(2)
print(my_list)  # Output: [10, 3, 4, 5, 6]
```

## List Operations

```python
# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition
repeated_list = [1] * 3
print(repeated_list)  # Output: [1, 1, 1]

# Length of a list
print(len(concatenated_list))  # Output: 6
```

## Common List Methods

- `append()`: Add an element to the end of the list.
- `extend()`: Extend the list by appending elements from another list.
- `insert()`: Insert an element at a specified position.
- `remove()`: Remove the first occurrence of a value from the list.
- `pop()`: Remove and return the element at the specified position.
- `index()`: Return the index of the first occurrence of a value.
- `count()`: Return the number of occurrences of a value.
- `sort()`: Sort the elements of the list in place.
- `reverse()`: Reverse the elements of the list in place.

## Conclusion

Lists are powerful and versatile data structures in Python, offering a wide range of operations for managing collections
of items efficiently.

# Tuple

## Introduction

A tuple in Python is an immutable collection of elements, similar to lists but with the key distinction of immutability.
Here are some key points about tuples:

- **Immutable Nature**: Tuples are immutable, meaning once created, their elements cannot be changed. This immutability
  makes iterating over tuples faster compared to lists.
- **Static Character**: Tuples ensure the integrity of data, as their contents cannot be altered after creation.
- **Ordered and Unchangeable**: Like lists, tuples maintain the order of elements, but unlike lists, they cannot be
  modified once created.
- **Usage in Dictionaries**: Tuples with immutable keys can be used as keys in dictionaries, providing a unique and
  unchangeable identifier.

## Sets

### Introduction

Sets in Python are collections of unique elements with no specific order. Here are some important characteristics of
sets:

- **Unique Values**: Sets store only unique elements, eliminating duplicates automatically.
- **Support for Logical Operations**: Sets support operations like union, intersection, and difference, making them
  useful for set theory operations.
- **Mutable**: Unlike tuples, sets are mutable, meaning their elements can be added or removed after creation.
- **Support for Hashing**: Sets support hashing, which allows for efficient membership testing.
- **No Slicing or Indexing**: Sets do not support slicing or indexing because they are unordered collections.

### Example

```python
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  # Output: {'cherry', 'banana', 'apple'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)  # Output: {'banana', 'papaya', 'mango', 'apple', 'pineapple', 'cherry'}
```

## Frozen Sets

### Introduction

Frozen sets in Python are similar to sets, but they are immutable. Once created, the elements of a frozen set cannot be
changed. Here are some key points about frozen sets:

- **Immutable**: Frozen sets, like tuples, are immutable collections, making them suitable for situations where
  immutability is desired.
- **Hashable Objects**: Frozen sets support hashable objects, enabling their use as elements in other sets or as keys in
  dictionaries.
- **Unordered**: Frozen sets, like sets, do not maintain a specific order of elements.
- **Similar to Mathematical Sets**: Frozen sets mirror mathematical sets, allowing for set operations like union,
  intersection, and difference.

## Dictionary

### Introduction

A dictionary in Python is an unordered collection of key-value pairs. Here are some key aspects of dictionaries:

- **Ordered**: Dictionaries maintain the order of insertion, preserving the sequence of key-value pairs.
- **Key-Value Pairs**: Each element in a dictionary consists of a key and its corresponding value.
- **Accessing by Keys**: Elements in a dictionary are accessed using their keys rather than numerical indices.
- **Mutable and Indexed**: Dictionaries are mutable, allowing for the addition, removal, and modification of key-value
  pairs.
- **Key Immunity**: Keys in dictionaries must be immutable types, such as strings, integers, or tuples.

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

---

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

# Exception Handling

![Error_Hierarchy.png](Assets/Error_Hierarchy.png)

- ## Try
  - ### Each try block should have one or more than one except block
- ## Except
  - ### One try can have multiple exceptions but one except cannot have multiple try
- ## Else
  - ### This block is accessed if the exception doesn't occur
- ## Finally
  - ### This is the block which ultimately works the least
- ## Raise
  - ### This is used to define Custom Exceptions, except blocks should be there to the corresponding raise block

---

```python
try:
    print(10/0)
except ArithmeticError as e:
    print("Exception Occur", e)
else:
    print("No exception occur")
finally:
    print("In the Finally Block")
print("Rest of the block")

try:
    print("In the Try Block")
except BaseException as e:
    print("Catching the Exception")
else:
    print("No Exception Occurs")
finally:
    print("In the Second Finally Block")
print("After the second block")
```

```commandline
Exception Occur division by zero
In the Finally Block
Rest of the block
In the Try Block
No Exception Occurs
In the Second Finally Block
After the second block

Process finished with exit code 0
```

### Default Exception Should always be in the last except or else it will not work

### Default Exception doesn't show the type of exception occuring thats why one may use BaseException Class

```python
try:
    print(10 / 0)

except TypeError as e:
    print("Exception Occur", e)
except: ## Default Exception
    print("It will not run")
else:
    print("No exception occur")
finally:
    print("In the Finally Block")
print("Rest of the block")

```

```commandline
It will not run
In the Finally Block
Rest of the block

Process finished with exit code 0
```

### We can Handle Multiple Exception in one Except Block

```python
try:
    print(10 / 0)
    print(15+ "k")
except (TypeError, ArithmeticError) as e:
    print("Exception Occur", e)
except:
    print("It will not run")
else:
    print("No exception occur")
finally:
    print("In the Finally Block")
print("Rest of the block")

```

```commandline
Exception Occur division by zero
In the Finally Block
Rest of the block

Process finished with exit code 0

```

### Finally block, no matter what will be executed

### Finally block is used in the cases where the application wants to run some specific functionaltity irrespective of the exception

```python
try:
    print("Hello")
finally:
    print("In the Finally Block")
print("Rest of the block")

```

```commandline
Hello
In the Finally Block
Rest of the block

Process finished with exit code 0

```

```python
try:
    print("Hello")
    print(10 / 0)
finally:
    print("In the Finally Block")
print("Rest of the block")

```

```commandline
Hello
In the Finally Block
Traceback (most recent call last):
  File "D:\Python Training\16 May\Prods\Class Codes\demo.py", line 3, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero

Process finished with exit code 1

```

### Finally doesnot have power to handle the exception only Except can do that, though it still will run and if the error is there the program will end abnormally

```python
try:
    num = int(input("Enter the number: "))
    print(10 / num)
    print(num + "k")
except (TypeError, ArithmeticError) as e:
    print("Exception Occur", e)
except:
    print("It will not run")
else:
    print("No exception occur")
finally:
    print("In the Finally Block")
print("Rest of the block")

```

```commandline
Enter the number: 5
2.0
Exception Occur unsupported operand type(s) for +: 'int' and 'str'
In the Finally Block
Rest of the block

Process finished with exit code 0
```

```commandline
Enter the number: 0
Exception Occur division by zero
In the Finally Block
Rest of the block

Process finished with exit code 0
```

### Finally will only work when the exception occurs in the try block

```python
print(10 / 0) ## Direct Exception
try:
    num = int(input("Enter the number: "))
    print(10 / num)
    print(num + "k")
except (TypeError, ArithmeticError) as e:
    print("Exception Occur", e)
except:
    print("It will not run")
else:
    print("No exception occur")
finally:
    print("In the Finally Block")
print("Rest of the block")

```

```commandline
Traceback (most recent call last):
  File "D:\Python Training\16 May\Prods\Class Codes\demo.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero

Process finished with exit code 1

```

### Another Ways where the finally won't work are

#### When os._exit(0)

```python
import os


try:
    num = int(input("Enter the number: "))
    print(num)
    os._exit(0)
except ValueError as e:
    print("Exception Occur", e)
except:
    print("It will not run")
else:
    print("No exception occur")
finally:
    print("In the Finally Block")
print("Rest of the block")

```

```commandline
Enter the number: 0
0

Process finished with exit code 0
```

#### And using os.abort()

```python
import os


try:
    num = int(input("Enter the number: "))
    print(num)
    os.abort()
except ValueError as e:
    print("Exception Occur", e)
except:
    print("It will not run")
else:
    print("No exception occur")
finally:
    print("In the Finally Block")
print("Rest of the block")

```

```commandline
Enter the number: 0
0


Process finished with exit code -1073740791 (0xC0000409)
```

## User Defined Exceptions

#### To raise your own exception from your own methods you need to use 'raise' keyword `raise ExceptionClassName("Your Information)`. By using `raise` keyword we can raise pre-defined and user-defined exceptions

```python
try:
    raise NameError("Hello")
except NameError as e:
    print("An Exception Occured", e)

```

```commandline
An Exception Occured Hello

Process finished with exit code 0
```

### We can generate exceptions as per our own requirements using raise keyword

```python
try:
    num = int(input("Enter the Number: "))
    if not num % 2 == 0:
        raise NameError("We are against Odd Numbers")
except NameError as e:
    print(e)

```

```commandline
Enter the Number: 3
We are against Odd Numbers

Process finished with exit code 0

```

```commandline
Enter the Number: 2

Process finished with exit code 0

```

### Custom Exceptions using Class

```python
class TooYoungException(Exception):
    def __init__(self, age):
        self.age = age


class TooOldException(Exception):
    def __init__(self, age):
        self.age = age


if __name__ == '__main__':
    age = int(input("Enter your Age: "))
    if age < 18:
        raise TooYoungException("You have to be 18 years old to join")
    elif age > 60:
        raise TooOldException("You are above the age limit")

```

```commandline
Enter your Age: 15
Traceback (most recent call last):
  File "D:\Python Training\16 May\Prods\Class Codes\demo.py", line 13, in <module>
    raise TooYoungException("You have to be 18 years old to join")
TooYoungException: You have to be 18 years old to join

Process finished with exit code 1
```

```commandline
Enter your Age: 90
Traceback (most recent call last):
  File "D:\Python Training\16 May\Prods\Class Codes\demo.py", line 15, in <module>
    raise TooOldException("You are above the age limit")
TooOldException: You are above the age limit

Process finished with exit code 1

```

```commandline
Enter your Age: 19

Process finished with exit code 0

```

## Exception Chaining

```python
def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e


if __name__ == '__main__':
    example()

```

```commandline
Traceback (most recent call last):
  File "D:\Python Training\16 May\Prods\Class Codes\demo.py", line 3, in example
    int('N/A')
ValueError: invalid literal for int() with base 10: 'N/A'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "D:\Python Training\16 May\Prods\Class Codes\demo.py", line 9, in <module>
    example()
  File "D:\Python Training\16 May\Prods\Class Codes\demo.py", line 5, in example
    raise RuntimeError('A parsing error occurred') from e
RuntimeError: A parsing error occurred

Process finished with exit code 1
```

# Python Modules

## Advantages of Python Modules

- **Simplicity**
  - Module often concentrates upon a specific problem in a big project and makes it easy to understand the code as it is
    segregated as per the use-cases
- **Maintainablity**
  - It makes the code easily accessible and easy to maintain and extend for future additions and updates

## In-Built Python Modules

- Math
- Random
- Os
- sys
- etc

```python
import math
print(math.sqrt(5))
```

```python
from math import sqrt, factorial
print(sqrt(5))
```

```python
import math as m
print(m.sqrt(5))
```

### ⬆ These are the ways to import a module in python

## Example of Modules

```python
# demo_module.py

city_list = ["indore", "delhi"]
```

```python
# demo.py

if __name__ == '__main__':
    from demo_module import city_list
    print(city_list)
```

```commandline
['indore', 'delhi']

Process finished with exit code 0
```

## Why should we not put all the code in try block?

## What is the hierarchy of except?

# Advanced Python (File Handling)

## Basic File Handling Operations

- **Open**
- **Read**
- **Write**
- **Close**
- **Rename**
- **Delete**

## File Handling Mode

- #### 'r' Read Mode
- #### 'w' Write Mode
- #### 'a' Append Mode
- #### 'r+' Read and Write Mode
- #### 'a+' Append and Read Mode

### If we want to use it in binary format just add b after the existing mode like 'rb', 'wb', etc.

---

## Syntax

```python
f = open(filename, mode)
```

## Serializing or Pickling

Converts python Objects into Byte Streams to be stored in a binary format

# File Handling in Python

## Pickling

- **dumps, dump**
- **loads, load**


