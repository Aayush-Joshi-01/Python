class Person(object):
    pass


class Male(Person):
    pass


class Female(Person):
    pass


if __name__ == '__main__':
    m = Male()
    mm = Male()
    print(id(m))
    print(id(mm))
