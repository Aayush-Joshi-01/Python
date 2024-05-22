import os

from colorama import Fore, Style

from BLACKJACK import black_jack
from HANGMAN.main import Hangman
from KBC.kaun_banega_crorepati import KBCGame
from Stone_Paper_Scissor.sps import Game
from TIC_TAC_TOE import tic_tac_toe


def clear_screen():
    if os.name == 'nt':  # for windows
        _ = os.system('cls')
    else:  # for mac and linux(here, os.name is 'posix')
        _ = os.system('clear')


def games_menu():
    os.system('color 0A')  # change bg color to light blue
    clear_screen()
    print(Fore.CYAN + Style.BRIGHT + "\tWelcome to the Yash Games Services!!!!")
    print(Fore.GREEN + Style.BRIGHT + "\t1> Black Jack")
    print(Fore.GREEN + Style.BRIGHT + "\t2> Tic Tac Toe")
    print(Fore.GREEN + Style.BRIGHT + "\t3> Kaun Banega Crorepati")
    print(Fore.GREEN + Style.BRIGHT + "\t4> Hangman")
    print(Fore.GREEN + Style.BRIGHT + "\t5> Stone Paper Scissor")
    print(Fore.CYAN + Style.BRIGHT + "\t6> Exit")


def get_terminal_size():
    try:
        return os.get_terminal_size()
    except OSError:
        return 80, 24  # Default terminal size


def print_centered(text):
    terminal_size = get_terminal_size()
    length = len(text)
    start_pos = (terminal_size[0] - length) // 2
    print(" " * start_pos + text)


if __name__ == '__main__':
    print_centered("Welcome to the Yash Games Services!!!!")
    while True:
        games_menu()
        choice = int(input(Fore.GREEN + Style.BRIGHT + "\tEnter the game you want to play: "))
        if not choice in [1, 2, 3, 4, 5, 6]:
            print(Fore.RED + "Invalid input. Please enter a number." + Fore.RESET)
            continue
        if choice == 1:
            black_jack.main()
        elif choice == 2:
            tic_tac_toe.main()
        elif choice == 3:
            KBCGame().start_game()
        elif choice == 4:
            Hangman().play()
        elif choice == 5:
            Game().play()
        elif choice == 6:
            print_centered("Thank you for using the Yash Games Services!!!!")
            break
