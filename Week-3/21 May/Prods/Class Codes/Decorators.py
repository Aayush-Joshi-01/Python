# A decorator is a function that takes another function as an argument and returns a modified version of that function
# For example, we can define a decorator that adds a message before and after the execution of a function
def add_message(func):
    # Define a wrapper function that will execute the original function and add the messages
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")

    # Return the wrapper function as the modified version of the original function
    return wrapper


# Define a simple function that prints "Hello world"
# def hello():
#     print("Hello world")


# Apply the decorator to the hello function using the @ syntax
@add_message
def hello():
    print("Hello world")


# Call the decorated hello function
hello()

# Output:
# Before calling the function
# Hello world
# After calling the function
# """ In programming decorators is a design pattern that add additional responsiblities to an object dynamically
# Decorator is a function, decorator is always going to take a fuction as argument and do some enhancements and return the same output fucntion
#
# This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time
# it is used to add new functionality

# use case of decorator logging test performance performance caching verify permission @csrfexempt we used in drf and also @login_required
# """
