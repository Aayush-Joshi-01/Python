from BLACKJACK.black_jack import BlackJack as black_jack_obj
def games_menu():
    print("1> Black Jack")
    print("2> Tic Tac Toe")
    print("3> Kaun Banega Crorepati")
    print("4> Hangman")


def black_jack_game():
    print("Welcome to the Game of Black Jack")
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        black_jack_obj.play_game()

if __name__ == '__main__':
    print("Welcome to the Yash Games Services!!!!")
    games_menu()

