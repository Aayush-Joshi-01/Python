import random

question_data = {
    "easy": [
        {
            "question": "What is the capital of India?",
            "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
            "answer": "a"
        },
        {
            "question": "Who is the CEO of Tesla?",
            "options": ["Elon Musk", "Jeff Bezos", "Mark Zuckerberg", "Bill Gates"],
            "answer": "a"
        },
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "answer": "a"
        },
        {
            "question": "Which planet is closest to the sun?",
            "options": ["Mercury", "Venus", "Earth", "Mars"],
            "answer": "a"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Blue Whale", "Elephant", "Giraffe", "Hippopotamus"],
            "answer": "a"
        },
        {
            "question": "Which country is known as the 'Land of the Rising Sun'?",
            "options": ["China", "Japan", "South Korea", "Vietnam"],
            "answer": "b"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
            "answer": ["William Shakespeare", "a"]
        },
        {
            "question": "What is the square root of 64?",
            "options": ["6", "7", "8", "9"],
            "answer": ["8", "c"]
        },
        {
            "question": "Which element has the atomic number 1?",
            "options": ["Hydrogen", "Helium", "Lithium", "Beryllium"],
            "answer": ["Hydrogen", "a"]
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Claude Monet"],
            "answer": ["Leonardo da Vinci", "a"]
        },
        {
            "question": "What is the smallest country in the world?",
            "options": ["Vatican City", "Monaco", "San Marino", "Liechtenstein"],
            "answer": ["Vatican City", "a"]
        },
        {
            "question": "Which language is spoken by the most people in the world?",
            "options": ["Mandarin Chinese", "English", "Hindi", "Spanish"],
            "answer": ["Mandarin Chinese", "a"]
        },
        {
            "question": "Who discovered penicillin?",
            "options": ["Alexander Fleming", "Louis Pasteur", "Marie Curie", "Thomas Edison"],
            "answer": ["Alexander Fleming", "a"]
        },
        {
            "question": "What is the tallest mountain in the world?",
            "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
            "answer": ["Mount Everest", "a"]
        },
        {
            "question": "Which country is home to the Great Barrier Reef?",
            "options": ["Australia", "New Zealand", "Indonesia", "Philippines"],
            "answer": ["Australia", "a"]
        },
        {
            "question": "Who composed the Four Seasons?",
            "options": ["Antonio Vivaldi", "Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven"],
            "answer": ["Antonio Vivaldi", "a"]
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
            "answer": ["Jupiter", "a"]
        },
        {
            "question": "Which animal is known as the 'Ship of the Desert'?",
            "options": ["Camel", "Llama", "Alpaca", "Giraffe"],
            "answer": ["Camel", "a"]
        },
        {
            "question": "What is the highest recorded temperature on Earth?",
            "options": ["149 °C", "200 °C", "300 °C", "400 °C"],
            "answer": ["300 °C", "a"]
        },
        {
            "question": "What is the main character in 'War and Peace'?",
            "options": ["Napoleon Bonaparte", "Peter Berg", "Anna Karenina", "Leo Tolstoy"],
            "answer": ["Leo Tolstoy", "a"]
        },
        {
            "question": "What is the highest point in the European Union?",
            "options": ["Mount Etna", "Mont Blanc", "Monte Ceneri", "Mont St. Michel"],
            "answer": ["Mont Blanc", "a"]
        },
        {
            "question": "What is the second planet from the sun?",
            "options": ["Mars", "Jupiter", "Saturn", "Venus"],
            "answer": ["Venus", "a"]
        },
        {
            "question": "What is the main difference between species and genera?",
            "options": ["Species have fewer genes, genera have more",
                        "Species are a type of plant, genera are a type of animal",
                        "Genera have a limited number of species, species can have thousands",
                        "Species are larger than genera"],
            "answer": ["Genera have a limited number of species, species can have thousands", "b"]
        },
        {
            "question": "Which language has the most native speakers in the world?",
            "options": ["English", "Mandarin Chinese", "Spanish", "Hindi"],
            "answer": ["Mandarin Chinese", "b"]
        },
        {
            "question": "Which of these elements is not found in nature?",
            "options": ["Beryllium", "Tin", "Uranium", "Helium"],
            "answer": ["Helium", "b"]
        },
        {
            "question": "Which composer is responsible for 'The Marriage of Figaro'?",
            "options": ["Antonio Vivaldi", "Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Ludwig van Beethoven"],
            "answer": ["Wolfgang Amadeus Mozart", "a"]
        },
    ],
    "medium": [
        {"question": "What is the currency of Japan?", "options": ["Yen", "Won", "Peso", "Dollar"],
         "answer": ["Yen", "a"]},
        {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Mercury", "Jupiter"],
         "answer": ["Mars", "a"]},
        {"question": "What is the tallest mammal on Earth?", "options": ["Giraffe", "Elephant", "Horse", "Rhino"],
         "answer": ["Giraffe", "a"]},
        {"question": "Which country is known as the Land of the Rising Sun?",
         "options": ["Japan", "China", "India", "Italy"], "answer": ["Japan", "a"]},
        {"question": "What is the chemical symbol for water?", "options": ["H2O", "CO2", "NaCl", "C6H12O6"],
         "answer": ["H2O", "a"]},
        {"question": "Who wrote 'To Kill a Mockingbird'?",
         "options": ["Harper Lee", "J.K. Rowling", "Stephen King", "Charles Dickens"], "answer": ["Harper Lee", "a"]},
        {"question": "Which famous scientist developed the theory of relativity?",
         "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Stephen Hawking"],
         "answer": ["Albert Einstein", "a"]},
        {"question": "Which ocean is the largest?",
         "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
         "answer": ["Pacific Ocean", "a"]},
        {"question": "Who painted the Mona Lisa?",
         "options": ["Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo"],
         "answer": ["Leonardo da Vinci", "a"]},
        {"question": "Which planet is closest to the Sun?", "options": ["Mercury", "Venus", "Earth", "Mars"],
         "answer": ["Mercury", "a"]},
        {"question": "What is the largest organ in the human body?", "options": ["Skin", "Heart", "Liver", "Brain"],
         "answer": ["Skin", "a"]},
        {"question": "Who is the author of '1984'?",
         "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.R.R. Tolkien"],
         "answer": ["George Orwell", "a"]},
        {"question": "Which gas is most abundant in Earth's atmosphere?",
         "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Argon"], "answer": ["Nitrogen", "a"]},
        {"question": "What is the largest desert in the world?", "options": ["Antarctica", "Sahara", "Arctic", "Gobi"],
         "answer": ["Antarctica", "a"]},
        {"question": "Who wrote 'The Great Gatsby'?", "options": ["F. Scott Fitzgerald", "Ernest Hemingway",
                                                                  "William Faulkner", "John Steinbeck"], "answer": [
            "F. Scott Fitzgerald", "a"]},
        {"question": "What is the chemical symbol for iron?", "options": ["Fe", "Ir", "In", "Au"],
         "answer": ["Fe", "a"]},
        {"question": "What is the capital of Brazil?",
         "options": ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"],
         "answer": ["Brasília", "a"]},
        {"question": "Who wrote 'The Catcher in the Rye'?",
         "options": ["J.D. Salinger", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
         "answer": ["J.D. Salinger", "a"]},
        {"question": "What is the chemical symbol for sodium?", "options": ["Na", "So", "Sd", "Ni"],
         "answer": ["Na", "a"]},
        {"question": "What is the largest organ in the human body?", "options": ["Skin", "Liver", "Heart", "Brain"],
         "answer": ["Skin", "a"]},
        {"question": "Who is the author of 'The Hobbit'?",
         "options": ["J.R.R. Tolkien", "C.S. Lewis", "J.K. Rowling", "George R.R. Martin"],
         "answer": ["J.R.R. Tolkien", "a"]},
        {"question": "What is the chemical symbol for silver?", "options": ["Ag", "Si", "Au", "Sr"],
         "answer": ["Ag", "a"]},

    ],
    "hard": [
        {"question": "Which of Shakespeare's plays is the longest?",
         "options": ["Hamlet", "Macbeth", "King Lear", "Othello"], "answer": ["Hamlet", "a"]},
        {"question": "What is the smallest prime number greater than 10?", "options": ["11", "13", "17", "19"],
         "answer": ["11", "a"]},
        {"question": "Who is the only U.S. president to serve more than two terms?",
         "options": ["Franklin D. Roosevelt", "George Washington", "Abraham Lincoln", "Thomas Jefferson"],
         "answer": ["Franklin D. Roosevelt", "a"]},
        {"question": "In which year did the Titanic sink?", "options": ["1912", "1907", "1920", "1915"],
         "answer": ["1912", "a"]},
        {"question": "Who composed the 'Moonlight Sonata'?",
         "options": ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Johannes Brahms"],
         "answer": ["Ludwig van Beethoven", "a"]},
        {"question": "What is the hardest natural substance on Earth?",
         "options": ["Diamond", "Graphene", "Quartz", "Tungsten"], "answer": ["Diamond", "a"]},
        {"question": "Who was the first woman to win a Nobel Prize?",
         "options": ["Marie Curie", "Rosalind Franklin", "Dorothy Hodgkin", "Barbara McClintock"],
         "answer": ["Marie Curie", "a"]},
        {"question": "Which war is considered the first 'world war'?",
         "options": ["Seven Years' War", "Napoleonic Wars", "Thirty Years' War", "World War I"],
         "answer": ["Seven Years' War", "a"]},
        {"question": "What is the capital of Australia?", "options": ["Canberra", "Sydney", "Melbourne", "Perth"],
         "answer": ["Canberra", "a"]},
        {"question": "Who invented the World Wide Web?",
         "options": ["Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Larry Page"], "answer": ["Tim Berners-Lee", "a"]},
        {"question": "What is the smallest bone in the human body?", "options": ["Stapes", "Incus", "Malleus", "Femur"],
         "answer": ["Stapes", "a"]},
        {"question": "Which two elements are liquid at room temperature?",
         "options": ["Mercury and Bromine", "Gold and Silver", "Carbon and Oxygen", "Helium and Neon"],
         "answer": ["Mercury and Bromine", "a"]},
        {"question": "What is the rarest blood type among humans?",
         "options": ["AB Negative", "O Negative", "B Negative", "A Negative"], "answer": ["AB Negative", "a"]},
        {"question": "Who was the first person to reach the South Pole?",
         "options": ["Roald Amundsen", "Robert Falcon Scott", "Ernest Shackleton", "Richard E. Byrd"],
         "answer": ["Roald Amundsen", "a"]},
        {"question": "What is the process by which plants make their own food called?",
         "options": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
         "answer": ["Photosynthesis", "a"]},
        {"question": "Which element has the highest melting point?",
         "options": ["Tungsten", "Carbon", "Titanium", "Platinum"], "answer": ["Tungsten", "a"]},
        {"question": "What is the collective name for a group of crows?",
         "options": ["Murder", "Flock", "Herd", "School"], "answer": ["Murder", "a"]},
        {"question": "Who developed the theory of evolution by natural selection?",
         "options": ["Charles Darwin", "Gregor Mendel", "Alfred Russel Wallace", "Jean-Baptiste Lamarck"],
         "answer": ["Charles Darwin", "a"]},
        {"question": "What is the longest river in South America?",
         "options": ["Amazon River", "Nile River", "Yangtze River", "Congo River"], "answer": ["Amazon River", "a"]},
        {"question": "Who painted 'The Persistence of Memory'?",
         "options": ["Salvador Dalí", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"],
         "answer": ["Salvador Dalí", "a"]}

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


class KBCGame:
    def __init__(self):
        self.questions = []
        self.lifelines = {"double_dip": 1, "50-50": 1, "flip_question": 1}
        self.current_question = 'Q1'
        self.checkpoints = ['Q5', 'Q10', 'Q15']
        self.final_earnings = 0

    def start_game(self):
        print("Welcome to Kaun Banega Crorepati!")
        print("You will be asked a series of questions, and you can use lifelines to help you.")
        print("You can quit the game at any time by entering 0.")
        self.select_questions()
        self.play_game()

    def select_questions(self):
        for number_of_question in range(0, 5):
            questions = question_data["easy"]
            random.shuffle(questions)
            self.questions.extend(questions[:5])
        print(len(questions))
        for number_of_question in range(5, 10):
            questions = question_data["medium"]
            random.shuffle(questions)
            self.questions.extend(questions[:5])
        print(len(questions))
        for number_of_question in range(10, 17):
            questions = question_data["hard"]
            random.shuffle(questions)
            self.questions.extend(questions[:7])
        print(len(questions))

    def play_game(self):
        for question in self.questions:
            print(f"\nQuestion: {question['question']}")
            print("Options:")
            for i, option in enumerate(question["options"]):
                print(f"{i + 1}. {option}")
            user_input = input("Enter your answer (or 0 to quit): ")
            if user_input == "0":
                self.final_earnings = self.current_amount
                print(f"You have quit the game with earnings of ₹{self.final_earnings}.")
                return
            self.process_answer(user_input, question)

    def process_answer(self, user_input, question):
        if user_input in question["answer"]:
            # self.current_amount = question["amount"]
            print(f"Correct! You have earned ₹{self.current_amount}.")
            if self.current_amount in self.checkpoints:
                print("You have reached a checkpoint!")
        else:
            print(f"Sorry, the correct answer is {question['answer']}.")
            self.game_over()

    def game_over(self):
        print("Game over!")
        print(f"Your final earnings are ₹{self.final_earnings}.")
        self.final_earnings = 0

    def use_lifeline(self, lifeline, question):
        if lifeline == "double_dip":
            if self.lifelines["double_dip"] > 0:
                self.lifelines["double_dip"] -= 1
                print("You have used the Double Dip lifeline. You can take two guesses.")
                user_input1 = input("Enter your first guess: ")
                user_input2 = input("Enter your second guess: ")
                if user_input1 in question["answer"] or user_input2 in question["answer"]:
                    print("Correct! You have earned ₹{self.current_amount}.")
                else:
                    print(f"Sorry, the correct answer is {question['answer']}.")
                    self.game_over()
            else:
                print("You have already used the Double Dip lifeline.")
        elif lifeline == "50-50":
            if self.lifelines["50-50"] > 0:
                self.lifelines["50-50"] -= 1
                print("You have used the 50-50 lifeline. Two incorrect options have been removed.")
                correct_index = question["options"].index(question["answer"])
                random.shuffle(question["options"])
                question["options"] = [question["options"][correct_index]] + question["options"][:2]
                user_input = input("Enter your answer: ")
                if user_input == question["answer"]:
                    print("Correct! You have earned ₹{self.current_amount}.")
                else:
                    print(f"Sorry, the correct answer is {question['answer']}.")
                    self.game_over()
            else:
                print("You have already used the 50-50 lifeline.")
        elif lifeline == "flip_question":
            if self.lifelines["flip_question"] > 0:
                self.lifelines["flip_question"] -= 1
                print("You have used the Flip Question lifeline. A new question will be presented.")
                self.select_questions()
                self.play_game()
            else:
                print("You have already used the Flip Question lifeline.")


if __name__ == "__main__":
    kbc_game = KBCGame()
    kbc_game.start_game()
