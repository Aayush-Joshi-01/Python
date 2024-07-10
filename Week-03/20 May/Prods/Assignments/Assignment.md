### 1. Count and Display the Total Number of Words in a Text File

```python
def count_words_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    print(f'Total number of words: {len(words)}')

    
count_words_in_file('example.txt')
```

### 2. Find and Display the Occurrence of the Word "the" in a Text File

```python
def count_the_occurrences(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
    words = text.split()
    the_count = words.count('the')
    print(f'The word "the" occurs {the_count} times')


count_the_occurrences('notes.txt')
```

### 3. Display Words Less Than 4 Characters from a Text File

```python
def display_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    short_words = [word for word in words if len(word) < 4]
    print('Words less than 4 characters:', short_words)


display_words('story.txt')
```

### 4. Count Specific Words in a Text File

```python
def count_specific_words(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
    words = text.split()
    this_count = words.count('this')
    these_count = words.count('these')
    print(f'The word "this" occurs {this_count} times')
    print(f'The word "these" occurs {these_count} times')


count_specific_words('article.txt')
```

### 5. Count Uppercase Characters in a Text File

```python
def count_uppercase_characters(filename):
    with open(filename, 'r') as file:
        text = file.read()
    uppercase_count = sum(1 for char in text if char.isupper())
    print(f'Total number of uppercase characters: {uppercase_count}')


count_uppercase_characters('example.txt')
```

### 6. Correct Specific Character Errors in a Text File

```python
def JTOI():
    with open('WORDS.TXT', 'r') as file:
        text = file.read()
    corrected_text = text.replace('J', 'I')
    print('Corrected content:')
    print(corrected_text)


JTOI()
```

### 7. Binary File Operations for Book Records

```python
import pickle

def createFile():
    with open('Book.dat', 'ab') as file:
        book = {}
        book['BookNo'] = input('Enter book number: ')
        book['Book_Name'] = input('Enter book name: ')
        book['Author'] = input('Enter author name: ')
        book['Price'] = float(input('Enter price: '))
        pickle.dump(book, file)

def countRec(author):
    count = 0
    try:
        with open('Book.dat', 'rb') as file:
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
```

### 8. Display Students with High Percentages from a Binary File

```python
import pickle

def count_rec():
    count = 0
    try:
        with open('student.dat', 'rb') as file:
            while True:
                try:
                    student = pickle.load(file)
                    if student['Percentage'] > 75:
                        print(student)
                        count += 1
                except EOFError:
                    break
    except FileNotFoundError:
        print('File not found')
    print(f'Number of students with percentage above 75: {count}')


count_rec()
```

### 9. Employee Records in a Binary File

```python
import pickle

def add_employee_record():
    with open('employee.dat', 'ab') as file:
        employee = {}
        employee['empcode'] = input('Enter employee code: ')
        employee['name'] = input('Enter name: ')
        employee['salary'] = float(input('Enter salary: '))
        pickle.dump(employee, file)

def display_high_salary_employees():
    try:
        with open('employee.dat', 'rb') as file:
            while True:
                try:
                    employee = pickle.load(file)
                    if employee['salary'] > 30000:
                        print(employee)
                except EOFError:
                    break
    except FileNotFoundError:
        print('File not found')


add_employee_record()
display_high_salary_employees()
```

### 10. Player Records in a Binary File

```python
import pickle

def display_players_starting_with_A():
    try:
        with open('players.dat', 'rb') as file:
            while True:
                try:
                    player = pickle.load(file)
                    if player['name'].startswith('A'):
                        print(player)
                except EOFError:
                    break
    except FileNotFoundError:
        print('File not found')

def count_players_from_country(country):
    count = 0
    try:
        with open('players.dat', 'rb') as file:
            while True:
                try:
                    player = pickle.load(file)
                    if player['country'] == country:
                        count += 1
                except EOFError:
                    break
    except FileNotFoundError:
        print('File not found')
    print(f'Number of players from {country}: {count}')

def add_player_record():
    with open('players.dat', 'ab') as file:
        player = {}
        player['code'] = input('Enter player code: ')
        player['name'] = input('Enter player name: ')
        player['country'] = input('Enter player country: ')
        player['total runs'] = int(input('Enter total runs: '))
        pickle.dump(player, file)


display_players_starting_with_A()
count_players_from_country('India')
add_player_record()
```
