# Python File Assignments

## 1. Count and Display the Total Number of Words in a Text File

Write a function in Python to count and display the total number of words in a text file.

## 2. Find and Display the Occurrence of the Word "the" in a Text File

Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the
occurrence of the word "the".

### Example:

If the content of the file is:

```

India is the fastest-growing economy. India is looking for more 

investments around the globe. The whole world is looking at India as a 

great market. Most of the Indians can foresee the heights that India is 

capable of reaching.

```

## 3. Display Words Less Than 4 Characters from a Text File

Write a function `display_words()` in Python to read lines from a text file "story.txt", and display those words which
are less than 4 characters.

## 4. Count Specific Words in a Text File

Write a function in Python to count the words "this" and "these" present in a text file "article.txt". Note that the
words "this" and "these" are complete words.

## 5. Count Uppercase Characters in a Text File

Write a function in Python to count uppercase characters in a text file.

## 6. Correct Specific Character Errors in a Text File

Aditi has used a text editing software to type some text. After saving the article as WORDS.TXT, she realized that she
has wrongly typed alphabet J in place of alphabet I everywhere in the article. Write a function definition for `JTOI()`
in Python that would display the corrected version of the entire content of the file WORDS.TXT with all the alphabets "
J" to be displayed as an alphabet "I" on screen.

### Example:

If Aditi has stored the following content in the file WORDS.TXT:

```

WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH 

THJS TO BE A SENTENCE

```

The function `JTOI()` should display the following content:

```

WELL, THIS IS A WORD BY ITSELF. YOU COULD STRETCH 

THIS TO BE A SENTENCE

```

## 7. Binary File Operations for Book Records

A binary file "Book.dat" has structure [BookNo, Book_Name, Author, Price].

### Tasks:

1. Write a user-defined function `createFile()` to input data for a record and add to Book.dat.

2. Write a function `countRec(Author)` in Python which accepts the Author name as a parameter and counts and returns the
   number of books by the given Author stored in the binary file "Book.dat".

## 8. Display Students with High Percentages from a Binary File

A binary file "student.dat" has structure (admission_number, Name, Percentage). Write a function `count_rec()` in Python
that would read contents of the file "STUDENT.DAT" and display the details of those students whose percentage is above
75%. Also, display the number of students scoring above 75%.

## 9. Employee Records in a Binary File

Given a binary file `employee.dat`, created using a dictionary object having keys: (empcode, name, and salary).

### Tasks:

1. Write a Python function that adds one more record at the end of the file.

2. Write a Python function that displays all employee records whose salary is more than 30,000.

## 10. Player Records in a Binary File

A binary file `players.dat`, containing records of the following list format: [code, name, country, and total runs].

### Tasks:

1. Write a Python function that displays all records where the player name starts from 'A'.

2. Write a Python function that accepts a country as an argument and counts and displays the number of players from that
   country.

3. Write a Python function that adds one record at the end of the file.