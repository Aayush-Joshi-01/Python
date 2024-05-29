def frequency(arg: dict, val: str) -> int:
    return sum(1 for argument in arg.values() if argument == val)


if __name__ == '__main__':
    print(frequency({1: 'hello', 2: 'hello', 3: 'hi'}, 'hello'))
