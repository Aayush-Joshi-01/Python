import os
import random

import gtts
from playsound3 import playsound


def convert_text_to_speech(text):
    tts = gtts.gTTS(text, lang='en')
    filename = 'output.mp3'
    tts.save(filename)
    playsound(filename)
    os.remove(filename)


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
            convert_text_to_speech("You went over, You lost!")
            return "You went over. You lose 😤"
        if user_score == computer_score:
            convert_text_to_speech("It ended in a Draw!")
            return "Draw 🙃"
        elif computer_score == 0:
            convert_text_to_speech("You lost Bro had a Blackjack")
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            convert_text_to_speech("You won with a BlackJack Congrats!")
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            convert_text_to_speech("Oh ho you went over, and you lost!")
            return "You went over. You lose 😭"
        elif computer_score > 21:
            convert_text_to_speech("Bruh Opponent went over, and you won!")
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            convert_text_to_speech("Well done you win!")
            return "You win 😃"
        else:
            convert_text_to_speech("You lost!")
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
            convert_text_to_speech(f"   Your cards: {user_cards}, current score: {user_score}")
            print(f"   Computer's first card: {computer_cards[0]}")
            convert_text_to_speech(f"   Computer's first card: {computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                convert_text_to_speech("Type 'y' to get another card or hit, type 'n' to pass or stall: ")
                user_should_deal = input("Type 'y' to get another card or hit, type 'n' to pass or stall: ")
                if user_should_deal == "y":
                    user_cards.append(self.deal_card())
                else:
                    is_game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(self.deal_card())
            computer_score = self.calculate_score(computer_cards)

        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        convert_text_to_speech(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
        convert_text_to_speech(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(self.compare())


def main():
    print(r""" 
 ____  _            _          _            _    
| __ )| | __ _  ___| | __     | | __ _  ___| | __
|  _ \| |/ _` |/ __| |/ /  _  | |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <  | |_| | (_| | (__|   < 
|____/|_|\__,_|\___|_|\_\  \___/ \__,_|\___|_|\_\
""")
    print("Welcome to the Game of Black Jack")
    convert_text_to_speech("Welcome to the game Blackjack!")
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        obj = BlackJack()
        obj.play_game()
