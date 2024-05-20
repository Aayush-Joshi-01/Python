import random
import time
import os
import gtts
from playsound3 import playsound

question_data = {
    "easy": [
        {
            "question": "What is the capital of India?",
            "options": ["Kolkata", "Chennai", "Mumbai", "Delhi"],
            "answer": "d"
        },
        {
            "question": "Who is the CEO of Tesla?",
            "options": ["Bill Gates", "Mark Zuckerberg", "Jeff Bezos", "Elon Musk"],
            "answer": "d"
        },
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Rome", "Paris", "London"],
            "answer": "c"
        },
        {
            "question": "Which planet is closest to the sun?",
            "options": ["Mars", "Venus", "Earth", "Mercury"],
            "answer": "d"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Giraffe", "Elephant", "Hippopotamus", "Blue Whale"],
            "answer": "d"
        },
        {
            "question": "Which country is known as the 'Land of the Rising Sun'?",
            "options": ["Vietnam", "China", "Japan", "South Korea"],
            "answer": "c"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["Mark Twain", "Charles Dickens", "William Shakespeare", "Jane Austen"],
            "answer": "c"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["7", "6", "9", "8"],
            "answer": "d"
        },
        {
            "question": "Which element has the atomic number 1?",
            "options": ["Beryllium", "Helium", "Lithium", "Hydrogen"],
            "answer": "d"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Claude Monet", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci"],
            "answer": "d"
        },
        {
            "question": "What is the smallest country in the world?",
            "options": ["Liechtenstein", "San Marino", "Monaco", "Vatican City"],
            "answer": "d"
        },
        {
            "question": "Which language is spoken by the most people in the world?",
            "options": ["English", "Spanish", "Hindi", "Mandarin Chinese"],
            "answer": "d"
        },
        {
            "question": "Who discovered penicillin?",
            "options": ["Thomas Edison", "Marie Curie", "Louis Pasteur", "Alexander Fleming"],
            "answer": "d"
        },
        {
            "question": "What is the tallest mountain in the world?",
            "options": ["Lhotse", "K2", "Kanchenjunga", "Mount Everest"],
            "answer": "d"
        },
        {
            "question": "Which country is home to the Great Barrier Reef?",
            "options": ["Philippines", "New Zealand", "Indonesia", "Australia"],
            "answer": "d"
        },
        {
            "question": "Who composed the Four Seasons?",
            "options": ["Ludwig van Beethoven", "Johann Sebastian Bach", "Antonio Vivaldi", "Wolfgang Amadeus Mozart"],
            "answer": "c"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Neptune", "Uranus", "Saturn", "Jupiter"],
            "answer": "d"
        },
        {
            "question": "Which animal is known as the 'Ship of the Desert'?",
            "options": ["Giraffe", "Llama", "Alpaca", "Camel"],
            "answer": "d"
        },
        {
            "question": "What is the highest recorded temperature on Earth?",
            "options": ["200 °C", "149 °C", "400 °C", "300 °C"],
            "answer": "d"
        },
        {
            "question": "What is the main character in 'War and Peace'?",
            "options": ["Peter Berg", "Anna Karenina", "Leo Tolstoy", "Napoleon Bonaparte"],
            "answer": "c"
        },
        {
            "question": "What is the highest point in the European Union?",
            "options": ["Monte Ceneri", "Mont St. Michel", "Mont Blanc", "Mount Etna"],
            "answer": "c"
        },
        {
            "question": "What is the second planet from the sun?",
            "options": ["Venus", "Mars", "Jupiter", "Saturn"],
            "answer": "a"
        },
        {
            "question": "What is the main difference between species and genera?",
            "options": [
                "Species are larger than genera",
                "Species have fewer genes, genera have more",
                "Genera have a limited number of species, species can have thousands",
                "Species are a type of plant, genera are a type of animal"
            ],
            "answer": "c"
        },
        {
            "question": "Which language has the most native speakers in the world?",
            "options": ["Hindi", "English", "Mandarin Chinese", "Spanish"],
            "answer": "c"
        },
        {
            "question": "Which of these elements is not found in nature?",
            "options": ["Tin", "Beryllium", "Helium", "Uranium"],
            "answer": "c"
        },
        {
            "question": "Which composer is responsible for 'The Marriage of Figaro'?",
            "options": ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven", "Antonio Vivaldi"],
            "answer": "b"
        }
    ],
    "medium": [
        {
            "question": "What is the currency of Japan?",
            "options": ["Dollar", "Won", "Yen", "Peso"],
            "answer": "c"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Jupiter", "Mercury", "Venus", "Mars"],
            "answer": "d"
        },
        {
            "question": "What is the tallest mammal on Earth?",
            "options": ["Horse", "Rhino", "Elephant", "Giraffe"],
            "answer": "d"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "Italy", "Japan", "India"],
            "answer": "c"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["CO2", "NaCl", "C6H12O6", "H2O"],
            "answer": "d"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Stephen King", "Charles Dickens", "J.K. Rowling", "Harper Lee"],
            "answer": "d"
        },
        {
            "question": "Which famous scientist developed the theory of relativity?",
            "options": ["Galileo Galilei", "Stephen Hawking", "Isaac Newton", "Albert Einstein"],
            "answer": "d"
        },
        {
            "question": "Which ocean is the largest?",
            "options": ["Arctic Ocean", "Indian Ocean", "Atlantic Ocean", "Pacific Ocean"],
            "answer": "d"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Pablo Picasso", "Vincent van Gogh", "Michelangelo", "Leonardo da Vinci"],
            "answer": "d"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Earth", "Mars", "Mercury"],
            "answer": "d"
        },
        {
            "question": "What is the largest organ in the human body?",
            "options": ["Heart", "Liver", "Brain", "Skin"],
            "answer": "d"
        },
        {
            "question": "Who is the author of '1984'?",
            "options": ["Aldous Huxley", "Ray Bradbury", "George Orwell", "J.R.R. Tolkien"],
            "answer": "c"
        },
        {
            "question": "Which gas is most abundant in Earth's atmosphere?",
            "options": ["Carbon Dioxide", "Argon", "Nitrogen", "Oxygen"],
            "answer": "c"
        },
        {
            "question": "What is the largest desert in the world?",
            "options": ["Gobi", "Antarctica", "Sahara", "Arctic"],
            "answer": "b"
        },
        {
            "question": "Who wrote 'The Great Gatsby'?",
            "options": ["Ernest Hemingway", "John Steinbeck", "F. Scott Fitzgerald", "William Faulkner"],
            "answer": "c"
        },
        {
            "question": "What is the chemical symbol for iron?",
            "options": ["Ir", "Au", "Fe", "In"],
            "answer": "c"
        },
        {
            "question": "What is the capital of Brazil?",
            "options": ["Salvador", "Rio de Janeiro", "São Paulo", "Brasília"],
            "answer": "d"
        },
        {
            "question": "Who wrote 'The Catcher in the Rye'?",
            "options": ["Ernest Hemingway", "F. Scott Fitzgerald", "Mark Twain", "J.D. Salinger"],
            "answer": "d"
        },
        {
            "question": "What is the chemical symbol for sodium?",
            "options": ["Sd", "Ni", "Na", "So"],
            "answer": "c"
        },
        {
            "question": "What is the largest organ in the human body?",
            "options": ["Heart", "Liver", "Brain", "Skin"],
            "answer": "d"
        },
        {
            "question": "Who is the author of 'The Hobbit'?",
            "options": ["C.S. Lewis", "George R.R. Martin", "J.K. Rowling", "J.R.R. Tolkien"],
            "answer": "d"
        },
        {
            "question": "What is the chemical symbol for silver?",
            "options": ["Si", "Sr", "Au", "Ag"],
            "answer": "d"
        }
    ],
    "hard": [
        {
            "question": "Which of Shakespeare's plays is the longest?",
            "options": ["King Lear", "Macbeth", "Othello", "Hamlet"],
            "answer": "d"
        },
        {
            "question": "What is the smallest prime number greater than 10?",
            "options": ["17", "13", "19", "11"],
            "answer": "d"
        },
        {
            "question": "Who is the only U.S. president to serve more than two terms?",
            "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "Franklin D. Roosevelt"],
            "answer": "d"
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1920", "1915", "1912", "1907"],
            "answer": "c"
        },
        {
            "question": "Who composed the 'Moonlight Sonata'?",
            "options": ["Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Johannes Brahms", "Ludwig van Beethoven"],
            "answer": "d"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["Graphene", "Quartz", "Diamond", "Tungsten"],
            "answer": "c"
        },
        {
            "question": "Who was the first woman to win a Nobel Prize?",
            "options": ["Barbara McClintock", "Rosalind Franklin", "Dorothy Hodgkin", "Marie Curie"],
            "answer": "d"
        },
        {
            "question": "Which war is considered the first 'world war'?",
            "options": ["Thirty Years' War", "World War I", "Napoleonic Wars", "Seven Years' War"],
            "answer": "d"
        },
        {
            "question": "What is the capital of Australia?",
            "options": ["Melbourne", "Perth", "Sydney", "Canberra"],
            "answer": "d"
        },
        {
            "question": "Who invented the World Wide Web?",
            "options": ["Steve Jobs", "Bill Gates", "Tim Berners-Lee", "Larry Page"],
            "answer": "c"
        },
        {
            "question": "What is the smallest bone in the human body?",
            "options": ["Incus", "Malleus", "Femur", "Stapes"],
            "answer": "d"
        },
        {
            "question": "Which two elements are liquid at room temperature?",
            "options": ["Gold and Silver", "Carbon and Oxygen", "Helium and Neon", "Mercury and Bromine"],
            "answer": "d"
        },
        {
            "question": "What is the rarest blood type among humans?",
            "options": ["B Negative", "A Negative", "O Negative", "AB Negative"],
            "answer": "d"
        },
        {
            "question": "Who was the first person to reach the South Pole?",
            "options": ["Ernest Shackleton", "Richard E. Byrd", "Roald Amundsen", "Robert Falcon Scott"],
            "answer": "c"
        },
        {
            "question": "What is the process by which plants make their own food called?",
            "options": ["Transpiration", "Fermentation", "Photosynthesis", "Respiration"],
            "answer": "c"
        },
        {
            "question": "Which element has the highest melting point?",
            "options": ["Carbon", "Titanium", "Tungsten", "Platinum"],
            "answer": "c"
        },
        {
            "question": "What is the collective name for a group of crows?",
            "options": ["School", "Herd", "Flock", "Murder"],
            "answer": "d"
        },
        {
            "question": "Who developed the theory of evolution by natural selection?",
            "options": ["Alfred Russel Wallace", "Jean-Baptiste Lamarck", "Gregor Mendel", "Charles Darwin"],
            "answer": "d"
        },
        {
            "question": "What is the longest river in South America?",
            "options": ["Yangtze River", "Congo River", "Amazon River", "Nile River"],
            "answer": "c"
        },
        {
            "question": "Who painted 'The Persistence of Memory'?",
            "options": ["Vincent van Gogh", "Claude Monet", "Salvador Dalí", "Pablo Picasso"],
            "answer": "c"
        }
    ]
}

question_amount = {
    "Q1": 1000,
    "Q2": 2000,
    "Q3": 3000,
    "Q4": 5000,
    "Q5": 10000,
    "Q6": 20000,
    "Q7": 40000,
    "Q8": 80000,
    "Q9": 160000,
    "Q10": 320000,
    "Q11": 640000,
    "Q12": 1250000,
    "Q13": 2500000,
    "Q14": 5000000,
    "Q15": 10000000,
    "Q16": 50000000,
    "Q17": 70000000
}


def convert_text_to_speech(text):
    tts = gtts.gTTS(text, lang='en')
    filename = 'output.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)


class KBCGame:
    def __init__(self):
        self.questions = []
        self.question_types = ["easy", "medium", "hard"]
        self.questions_numbers = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q9', 'Q8', 'Q9', 'Q10', 'Q11',
                                  'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17']
        self.question_count = {"easy": 5, "medium": 5, "hard": 7}
        self.lifelines = {"double_dip": 1, "50-50": 1, "flip_question": 1}
        self.checkpoints = ['Q5', 'Q10', 'Q15']
        self.final_earnings = 0
        self.current_question_index = 0

    def start_game(self):
        ascii_art = r"""
            .------------------------------------------------------------.
            |                                                            |
            | _  __                   ____                               |
            || |/ /__ _ _   _ _ __   | __ )  __ _ _ __   ___  __ _  __ _ |
            || ' // _` | | | | '_ \  |  _ \ / _` | '_ \ / _ \/ _` |/ _` ||
            || . \ (_| | |_| | | | | | |_) | (_| | | | |  __/ (_| | (_| ||
            ||_|\_\__,_|\__,_|_| |_| |____/ \__,_|_| |_|\___|\__, |\__,_||
            | / ___|_ __ ___  _ __ ___ _ __   __ _| |_(_)    |___/       |
            || |   | '__/ _ \| '__/ _ \ '_ \ / _` | __| |                |
            || |___| | | (_) | | |  __/ |_) | (_| | |_| |                |
            | \____|_|  \___/|_|  \___| .__/ \__,_|\__|_|                |
            |                         |_|                                |
            |                                                            |
            '------------------------------------------------------------'
        """
        print(ascii_art)
        print("Welcome to Kaun Banega Crorepati!")
        playsound("Assets/Intro.mp3")
        print("You will be asked a series of questions, and you can use lifelines to help you.")
        print("You can quit the game at any time by entering 0.")
        while True:
            self.select_questions()
            self.play_game()
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
            self.reset_game()

    def reset_game(self):
        self.questions = []
        self.final_earnings = 0
        self.current_question_index = 0

    def select_questions(self):
        for question_type in self.question_types:
            questions = question_data[question_type]
            random.shuffle(questions)
            self.questions.extend(questions[:self.question_count[question_type]])
        random.shuffle(self.questions)

    def play_game(self):
        for question in self.questions:
            self.current_question_index += 1
            print(f"\nQuestion: {question['question']}")
            convert_text_to_speech(question['question'])
            print("Options:")
            convert_text_to_speech("Options are ")
            for option_id, option in zip('abcd', question["options"]):
                print(f"{option_id}. {option}")
                convert_text_to_speech(f"{option_id}. {option}")

            while True:
                user_input = input("Enter your answer (or 0 to quit, or 'l' to use a lifeline): ").strip().lower()
                if user_input == "":
                    print("Please provide an answer.")
                elif user_input == 'l':

                    lifeline_choice = self.lifelines_menu()
                    if lifeline_choice == '1':
                        correct_answer = self.use_lifeline("double_dip", question)
                        if correct_answer:
                            break
                    elif lifeline_choice == '2':
                        correct_answer = self.use_lifeline("50-50", question)
                        if correct_answer:
                            break
                    elif lifeline_choice == '3':
                        self.use_lifeline("flip_question", question)
                elif user_input not in ['a', 'b', 'c', 'd', '0']:
                    print("Invalid input. Please enter a valid option (a, b, c, d) or 0 to quit.")
                else:
                    break
            if user_input == "0":
                if self.current_question_index == 1:
                    self.final_earnings = 0
                else:
                    self.final_earnings = question_amount[self.questions_numbers[self.current_question_index - 2]]
                print(f"You have quit the game with earnings of ₹{self.final_earnings}.")
                return
            elif user_input == 'l':
                continue
            if not self.process_answer(user_input, question):
                break
        else:
            playsound("Assets/7Crore.mp3")
            time.sleep(4)
            self.final_earnings = self.calculate_final_earnings()
            print(f"Congratulations! You've answered all questions correctly.")

    def process_answer(self, user_input, question):
        if user_input in question["answer"]:
            current_question_number = self.get_current_question_number()
            earnings = question_amount[current_question_number]
            print(f"Correct! You have earned ₹{earnings}.")
            if current_question_number in self.checkpoints:
                print("You have reached a checkpoint!")
                convert_text_to_speech("You have reached a checkpoint!")
            return True
        else:
            correct_option = question["options"][ord(question["answer"]) - ord('a')]
            print(f"Sorry, the correct answer is {correct_option}.")
            self.game_over()
            return False

    def game_over(self):
        print("Game over!")
        self.final_earnings = self.calculate_final_earnings()
        print(f"Your final earnings are ₹{self.final_earnings}.")

    def calculate_final_earnings(self):
        last_checkpoint_earned = 0
        for checkpoint in self.checkpoints:
            if int(checkpoint[1:]) <= self.current_question_index:
                last_checkpoint_earned = question_amount[checkpoint]
        return max(last_checkpoint_earned, 0)

    def get_current_question_number(self):
        return f"Q{self.current_question_index}"

    def use_lifeline(self, lifeline, question):
        if lifeline == "double_dip":
            if self.lifelines["double_dip"] > 0:
                self.lifelines["double_dip"] -= 1
                print("You have used the Double Dip lifeline. You can take two guesses.")
                user_input1 = input("Enter your first guess: ").strip().lower()
                user_input2 = input("Enter your second guess: ").strip().lower()
                if user_input1 in question["answer"] or user_input2 in question["answer"]:
                    current_question_number = self.get_current_question_number()
                    earnings = question_amount[current_question_number]
                    print(f"Correct! You have earned ₹{earnings}.")
                    if current_question_number in self.checkpoints:
                        print("You have reached a checkpoint!")
                    return True
                else:
                    print(f"Sorry, the correct answer is {question['answer']}.")
                    self.game_over()
                    return False
            else:
                print("You have already used the Double Dip lifeline.")
                return False
        elif lifeline == "50-50":
            if self.lifelines["50-50"] > 0:
                self.lifelines["50-50"] -= 1
                print("You have used the 50-50 lifeline. Two incorrect options have been removed.")
                correct_index = ord(question["answer"]) - ord('a')
                options_copy = question["options"][:]
                options_copy.pop(correct_index)
                removed_options = options_copy[:2]
                for option_id, option in zip('abcd', question["options"]):
                    if option not in removed_options:
                        print(f"{option_id}. {option}")
                user_input = input("Enter your answer: ").strip().lower()
                if user_input == question["answer"]:
                    current_question_number = self.get_current_question_number()
                    earnings = question_amount[current_question_number]
                    print(f"Correct! You have earned ₹{earnings}.")
                    if current_question_number in self.checkpoints:
                        print("You have reached a checkpoint!")
                    return True
                else:
                    print(f"Sorry, the correct answer is {question['answer']}.")
                    self.game_over()
                    return False
            else:
                print("You have already used the 50-50 lifeline.")
                return False
        elif lifeline == "flip_question":
            if self.lifelines["flip_question"] > 0:
                self.lifelines["flip_question"] -= 1
                print("You have used the Flip Question lifeline. A new question will be presented.")
                self.questions.remove(question)
                self.questions.append(question)
                return
            else:
                print("You have already used the Flip Question lifeline.")
                return False

    @staticmethod
    def lifelines_menu():
        print("Choose a lifeline:")
        print("1. Double Dip")
        print("2. 50-50")
        print("3. Flip Question")
        while True:
            choice = input("Enter your choice (1-3): ").strip()
            if choice in ['1', '2', '3']:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")


if __name__ == "__main__":
    kbc_game = KBCGame()
    kbc_game.start_game()
