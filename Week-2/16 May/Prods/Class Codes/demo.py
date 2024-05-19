# from demo_module import city_list
# print(city_list)

# from tqdm import tqdm
# import time
#
# for i in tqdm(range(101),
#               desc="Loading…",
#               ascii=False, ncols=75):
#     time.sleep(0.01)
#
# print("Complete.")
# import time
#
# for remaining in range(10, 0, -1):
#     print(remaining, end='', flush=True)
#     time.sleep(1)
#     print(end='\r')
#
# print("Time's up!")


import threading
import time
import random
import sys
import winsound


def display_question(question, options, countdown):
    print(question)
    for j, option in enumerate(options, 1):
        print(f"{j}. {option}")
    if countdown is not None:
        print(f"Time Left for Question: {countdown} sec")


def fifty_fifty_lifeline(options, correct_option_index):
    options_copy = options[:]
    options_copy.pop(correct_option_index)
    incorrect_option_index = random.choice(range(len(options_copy)))
    incorrect_option = options_copy[incorrect_option_index]
    options_remaining = [options[correct_option_index], incorrect_option]
    print(f"The options have been reduced to two: {options_remaining[0]} and {options_remaining[1]}")
    options.remove(incorrect_option)


def flip_question_lifeline(flipped_questions):
    question_index = random.randint(0, len(flipped_questions) - 1)
    question = flipped_questions.pop(question_index)
    print("The question has been flipped!")
    display_question(question['question'], question['options'], None)
    return question


def double_dip_lifeline(question_number, questions):
    print("You chose Double Dip! You will have two attempts to answer this question.")
    user_choice = int(input("Enter your first choice (1-4): ")) - 1
    if user_choice == questions[question_number]['answer']:
        print("Correct! You still have one more attempt.")
        user_choice = int(input("Enter your second choice (1-4): ")) - 1
        if user_choice != questions[question_number]['answer']:
            print("Wrong answer. But you still have one more attempt.")
    else:
        print("Wrong answer. Game over!")
        return False
    return True

def timer(countdown):
    while countdown > 0:
        print(f"{countdown} seconds is the time left", end='\r')
        time.sleep(1)
        countdown -= 1
        if countdown <= 5:
            winsound.Beep(1000, 100)
    print("Time's up!")
    sys.exit()
# def timer(countdown):
#     while countdown > 0:
#         time.sleep(1)
#         countdown -= 1
#         sys.stdout.write(f"\rTime Left for Question: {countdown} sec")
#         sys.stdout.flush()
#         if countdown <= 5:
#             winsound.Beep(1000, 100)
#     print("\nTime's up!")
#     sys.exit()


def quiz_game(questions):
    score = 0
    points = 1000
    fifty_fifty_used = False
    flip_question_used = False
    double_dip_used = False
    flipped_questions = questions[:]

    for question_number in range(len(questions)):
        if question_number < 5:
            countdown = 30
        elif 5 <= question_number < 10:
            countdown = 60
        else:
            countdown = None

        # Define a flag to indicate if the thread should stop
        stop_flag = threading.Event()

        # Define the function that sets the flag to stop the thread
        def stop_timer():
            stop_flag.set()

        # Create the thread with the timer function and pass the countdown value as an argument
        timer_thread = threading.Thread(target=timer, args=(10,))  # Assuming countdown starts from 10

        # Start the thread
        timer_thread.start()
        display_question(f"Question {question_number + 1}: {questions[question_number]['question']}",
                         questions[question_number]['options'], countdown)
        print("Current Score:", score)

        while True:

            user_choice = input("Enter your choice (1-5): ")
            if user_choice.isdigit() and 1 <= int(user_choice) <= 5:
                user_choice = int(user_choice) - 1

                if user_choice == 4:
                    print("1. 50/50  2. Flip the question  3. Double Dip")
                    lifeline_choice = int(input("Choose lifeline: "))
                    if lifeline_choice == 1 and not fifty_fifty_used:
                        fifty_fifty_lifeline(questions[question_number]['options'],
                                             questions[question_number]['answer'])
                        fifty_fifty_used = True
                    elif lifeline_choice == 2 and not flip_question_used:
                        flipped_question = flip_question_lifeline(flipped_questions)
                        flip_question_used = True
                    elif lifeline_choice == 3 and not double_dip_used:
                        double_dip_used = double_dip_lifeline(question_number, questions)
                        if not double_dip_used:
                            break
                    else:
                        print("Invalid lifeline choice. Please choose a different lifeline or enter your answer.")
                else:
                    if user_choice == questions[question_number]['answer']:
                        if question_number < 5:
                            score += points
                            points += 1000
                        else:
                            score += points
                            points *= 2
                        break  # Break the loop when the correct answer is chosen
                    else:
                        print("Wrong answer! Please try again.")
                        # timer_thread.do_run = False  # Stop the timer thread
                        # timer_thread.do_run = False
                        # timer_thread.join()
                        stop_timer()
                        timer_thread.join()
                        break  # Break the loop when the answer is incorrect
            else:
                print("Invalid input. Please enter a number between 1 and 5.")

    print(f"Your final score is: {score}")


questions = [
    {"question": "What is the capital of France?",
     "options": ["Paris", "London", "Berlin", "Madrid", "Choose lifeline"], "answer": 0},
    {"question": "What is the largest planet in our solar system?",
     "options": ["Earth", "Jupiter", "Mars", "Venus", "Choose lifeline"], "answer": 1},
    {"question": "Who wrote 'Romeo and Juliet'?",
     "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain", "Choose lifeline"],
     "answer": 0},
    {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Fe", "Cu", "Choose lifeline"],
     "answer": 0},
    {"question": "What is the capital of Australia?",
     "options": ["Sydney", "Melbourne", "Canberra", "Brisbane", "Choose lifeline"], "answer": 2},
    {"question": "What is the largest ocean on Earth?",
     "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", "Choose lifeline"], "answer": 2},
    {"question": "Who painted the Mona Lisa?",
     "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo", "Choose lifeline"],
     "answer": 1},
    {"question": "What is the national animal of China?",
     "options": ["Panda", "Tiger", "Elephant", "Lion", "Choose lifeline"], "answer": 0},
    {"question": "Which planet is known as the 'Red Planet'?",
     "options": ["Jupiter", "Mars", "Saturn", "Neptune", "Choose lifeline"], "answer": 1},
    {"question": "Who is known as the 'Father of Computers'?",
     "options": ["Alan Turing", "Charles Babbage", "Steve Jobs", "Bill Gates", "Choose lifeline"], "answer": 1},
    {"question": "What is the largest mammal in the world?",
     "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus", "Choose lifeline"], "answer": 1},
    {"question": "Which country is known as the Land of the Rising Sun?",
     "options": ["China", "Japan", "India", "Australia", "Choose lifeline"], "answer": 1},
    {"question": "Who is the author of 'To Kill a Mockingbird'?",
     "options": ["Harper Lee", "J.K. Rowling", "Stephen King", "George Orwell", "Choose lifeline"], "answer": 0},
    {"question": "What is the chemical symbol for water?", "options": ["W", "H2", "H2O", "O", "Choose lifeline"],
     "answer": 2},
    {"question": "Which organ is responsible for pumping blood throughout the body?",
     "options": ["Heart", "Liver", "Lungs", "Kidneys", "Choose lifeline"], "answer": 0},
    {"question": "What is the capital of Canada?",
     "options": ["Toronto", "Montreal", "Ottawa", "Vancouver", "Choose lifeline"], "answer": 2}
]

quiz_game(questions)

#
# import threading
# import time
#
# def timer(countdown):
#     while countdown > 0:
#         print(countdown, end='\r')
#         time.sleep(1)
#         countdown -= 1
#     print("Time's up!")
#
# # Define a flag to indicate if the thread should stop
# stop_flag = threading.Event()
#
# # Define the function that sets the flag to stop the thread
# def stop_timer():
#     stop_flag.set()
#
# # Create the thread with the timer function and pass the countdown value as an argument
# timer_thread = threading.Thread(target=timer, args=(10,))  # Assuming countdown starts from 10
#
# # Start the thread
# timer_thread.start()
#
# # Let the thread run for a while
# time.sleep(5)  # Let it run for 5 seconds
#
# # Stop the thread
# stop_timer()
# timer_thread.join()
