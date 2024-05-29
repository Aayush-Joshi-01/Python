import pickle


def createFile():
    with open('Assets/Book.dat', 'ab') as file:
        book = {}
        book['BookNo'] = input('Enter book number: ')
        book['Book_Name'] = input('Enter book name: ')
        book['Author'] = input('Enter author name: ')
        book['Price'] = float(input('Enter price: '))
        pickle.dump(book, file)


def countRec(author):
    count = 0
    try:
        with open('Assets/Book.dat', 'rb') as file:
            while True:
                try:
                    book = pickle.load(file)
                    if book['Author'] == author:
                        count += 1
                except EOFError:
                    break
    except FileNotFoundError:
        print('File not found')
    return count


createFile()
print(countRec('Author Name'))
