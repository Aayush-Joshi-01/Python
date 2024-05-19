# we are having a astring and integer
# list = [123,45,56, 'hello']
# is addition of number  remove that number and write even there
# if string have more than 5 character remove it
def func(example):
    for iterator in range(len(example)):
        arg = str(example[iterator])
        if arg.isdigit():
            if sum(int(digit) for digit in str(arg)) % 2 != 0:
                example[iterator] = "even"
        elif isinstance(arg, str) and len(arg) > 5:
            example.remove(arg)
    return example


if __name__ == '__main__':
    example = [123, 45, 56, 'hello', 'hi', 'aayush']
    print(func(example))
