from BLACKJACK import black_jack
from HANGMAN.main import Hangman
from Projects.Y_Games.KBC.kaun_banega_crorepati import KBCGame
from TIC_TAC_TOE import tic_tac_toe


def games_menu():
    print("1> Black Jack")
    print("2> Tic Tac Toe")
    print("3> Kaun Banega Crorepati")
    print("4> Hangman")


if __name__ == '__main__':
    print("Welcome to the Yash Games Services!!!!")
    games_menu()
    while True:
        choice = int(input("Enter the game you want to play: "))
        if not choice in [1, 2, 3, 4, 0]:
            print("Enter a valid Choice!!")
            continue
        if choice == 1:
            black_jack.main()
        if choice == 2:
            tic_tac_toe.main()
        if choice == 3:
            KBCGame().start_game()
        if choice == 4:
            Hangman().play()
        if choice == 0:
            print("Thank you for using the Yash Games Services!!!!")
            break
        games_menu()
