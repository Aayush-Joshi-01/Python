from flask import Flask

from BLACKJACK import black_jack
from Projects.Y_Games.KBC.kaun_banega_crorepati import KBCGame
from TIC_TAC_TOE.tic_tac_toe import TicTacToe as TicTacToe, HumanPlayer, ComputerPlayer


def kbc():
    kbc_game = KBCGame()
    kbc_game.start_game()


def games_menu():
    print("1> Black Jack")
    print("2> Tic Tac Toe")
    print("3> Kaun Banega Crorepati")
    print("4> Hangman")


def tictactoe():
    ttt = TicTacToe()
    player1 = HumanPlayer('Player 1', 'X')
    mode = input("Choose mode: 1 for 2-player, 2 for computer: ")
    if mode == '1':
        player2 = HumanPlayer('Player 2', 'O')
    else:
        player2 = ComputerPlayer('Computer', 'O')

    while True:
        result = ttt.play_game(player1, player2)
        print(f"Scores: {ttt.scores}")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            break


def black_jack_game():
    black_jack.main()


app = Flask(__name__)


@app.route('/game', methods=['GET'])
def play_game():
    print("Welcome to the Yash Games Services!!!!")
    games_menu()
    while True:
        choice = int(input("Enter the game you want to play: "))
        if not choice in [1, 2, 3, 4, 0]:
            print("Enter a valid Choice!!")
            continue
        if choice == 1:
            black_jack_game()
        if choice == 2:
            tictactoe()
        if choice == 3:
            kbc()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
