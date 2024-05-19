def outer_function():
    print("Outer Function")

    def inner_function():
        print("Inner Function")

    return inner_function


if __name__ == '__main__':
    func = outer_function()()
