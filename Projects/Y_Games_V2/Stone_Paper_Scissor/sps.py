import random


class Game:
    def __init__(self):
        self.options = ["rock", "paper", "scissors"]

    def get_user_choice(self):
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in self.options:
            print("Invalid input. Please try again.")
            return self.get_user_choice()
        return user_choice

    def get_computer_choice(self):
        return random.choice(self.options)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "scissors" and computer_choice == "paper") or \
                (user_choice == "paper" and computer_choice == "rock"):
            return "user"
        else:
            return "computer"

    def play(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f"User chose {user_choice.capitalize()}, computer chose {computer_choice.capitalize()}.")
        winner = self.determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
        else:
            print("Computer wins!")


if __name__ == "__main__":
    game = Game()
    game.play()
