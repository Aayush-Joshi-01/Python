import random


class BlackJack:
    @staticmethod
    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    @staticmethod
    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    @staticmethod
    def compare():
        if user_score > 21 and computer_score > 21:
            return "You went over. You lose 😤"
        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"

    def play_game(self):
        global computer_score, user_score
        user_cards = []
        computer_cards = []
        is_game_over = False

        for _ in range(2):
            user_cards.append(self.deal_card())
            computer_cards.append(self.deal_card())

        while not is_game_over:
            user_score = self.calculate_score(user_cards)
            computer_score = self.calculate_score(computer_cards)
            print(f"   Your cards: {user_cards}, current score: {user_score}")
            print(f"   Computer's first card: {computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                user_should_deal = input("Type 'y' to get another card or hit, type 'n' to pass or stall: ")
                if user_should_deal == "y":
                    user_cards.append(self.deal_card())
                else:
                    is_game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(self.deal_card())
            computer_score = self.calculate_score(computer_cards)

        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(self.compare())


def main():
    print("Welcome to the Game of Black Jack")
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        obj = BlackJack()
        obj.play_game()
