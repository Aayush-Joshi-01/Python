if __name__ == '__main__':
    file = open('data.txt', 'r+')
    print(file.read())
    file.write(" Hello World")
    print(file.read())
    file.close()
