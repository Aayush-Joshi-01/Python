class Demo:
    def __init__(self, value):
        self.value = value

    def __del__(self):
        print(f"Object {self.value} is deleted")


if __name__ == '__main__':
    obj1 = Demo(1)
    obj2 = Demo(2)
    obj3 = Demo(3)
    del obj1
    del obj2
    del obj3
