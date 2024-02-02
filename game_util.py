def convert_game(game):
    # print(game.keys())

    res = {}
    stats = ['player', 'date_game', 'team_id', 'opp_id', 'game_location', 'mp', 'fg', 'fga', 'fg3', 'fg3a', 'ft', 'fta',
             'orb', 'drb', 'ast', 'stl', 'blk', 'pts']
    f_name, l_name = game['player'].split()

    # print(game)
    # print(len(game))

    if len(game) == 30:
        res['game_id'] = game['team_id'] + '_' + game['opp_id'] + game['date_game']

        for stat in stats:
            try:
                if stat == 'game_location':
                    if game[stat] == '@':
                        res[stat] = True
                    else:
                        res[stat] = False
                else:
                    res[stat] = game[stat]
            except:
                print('convert error')
                continue
        # print(res)
        return res
    else:
        return None

