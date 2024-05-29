# You're building a program to process user input for a quiz application.
# Write a Python function to shuffle the order of questions in a quiz given a list of questions

import random


def shuffle_questions(questions):
    random.shuffle(questions)
    return questions


if __name__ == '__main__':
    questions = [
        "What is the capital of France?",
        "What is the capital of India?",
        "What is the capital of Germany?",
        "What is the capital of China?",
        "What is the capital of United States?",
        "What is the capital of Russia?",
        "What is the capital of Brazil?",
        "What is the capital of Argentina?",
        "What is the capital of Canada?",
        "What is the capital of Mexico?",
    ]
    for question in shuffle_questions(questions):
        print(question)
