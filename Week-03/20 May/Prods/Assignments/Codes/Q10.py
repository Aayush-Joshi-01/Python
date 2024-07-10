import pickle


def display_players_starting_with_A():
    try:
        with open('Assets/players.dat', 'rb') as file:
            while True:
                try:
                    player = pickle.load(file)
                    if player['name'].startswith('A'):
                        print(player)
                except EOFError:
                    break
    except FileNotFoundError:
        print('File not found')


def count_players_from_country(country):
    count = 0
    try:
        with open('Assets/players.dat', 'rb') as file:
            while True:
                try:
                    player = pickle.load(file)
                    if player['country'] == country:
                        count += 1
                except EOFError:
                    break
    except FileNotFoundError:
        print('File not found')
    print(f'Number of players from {country}: {count}')


def add_player_record():
    with open('Assets/players.dat', 'ab') as file:
        player = {}
        player['code'] = input('Enter player code: ')
        player['name'] = input('Enter player name: ')
        player['country'] = input('Enter player country: ')
        player['total runs'] = int(input('Enter total runs: '))
        pickle.dump(player, file)


add_player_record()
display_players_starting_with_A()
count_players_from_country('India')
