import random


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.scores = {'Player 1': 0, 'Player 2': 0, 'Computer': 0}

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print()

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

    def play_game(self, player1, player2):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        letter = 'X'
        while self.empty_squares():
            if letter == 'O':
                square = player2.get_move(self)
            else:
                square = player1.get_move(self)
            if self.make_move(square, letter):
                if self.current_winner:
                    self.print_board()
                    if letter == 'X':
                        self.scores[player1.name] += 1
                    else:
                        self.scores[player2.name] += 1
                    print(f"{letter} wins!")
                    return letter
                letter = 'O' if letter == 'X' else 'X'
            self.print_board()
        print("It's a tie!")
        return 'Draw'


class HumanPlayer:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.name + ' (' + self.letter + ')' + ' Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class ComputerPlayer:
    def __init__(self, name, letter):
        self.name = name
        self.letter = letter

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


def main():
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


if __name__ == '__main__':
    main()
