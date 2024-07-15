if __name__ == '__main__':
    file = open('data.txt', 'w')
    print(file.readable())
    print(file.writable())
    print(file.mode)
    print(file.name)
    print(file.closed)
    file.close()
    print(file.closed)
