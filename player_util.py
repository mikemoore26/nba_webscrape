
def get_player_list(year):
    filename = f'./data/players_list_{year}.txt'

    with open(filename, 'r') as f:
        players = f.read()

    return players.split(';')


def convert_player_name(playername):
    playername = playername.replace('.', '')
    playername = playername.split()
    fname = playername[0]
    lname = playername[1]
    if len(fname) >= 2:
        fname = fname[:2]
    if len(lname) >= 5:
        lname = lname[:5]
    return fname, lname