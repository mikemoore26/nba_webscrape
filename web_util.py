import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
import pandas as pd
import time
import game_util

driver_loc = "/Users/michaelmoore/PycharmProjects/chromedriver"


def get_data(players, year,sleep=5, retries=3):
    from player_util import convert_player_name
    master_list = []
    failed_names = []

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Chrome()

    failed = False

    for player in players:
        print(f"{player} - {year}")
        try:
            first_name, last_name = convert_player_name(player)
            p_name = first_name + last_name
        except:
            failed_names.append({'name': first_name+' ' + last_name,'pname': p_name, 'year': year})
            print(failed_names)
            continue

        url = f"https://www.basketball-reference.com/players/{last_name[0]}/{last_name[:5]}{first_name[:2]}01/gamelog/{year}"
        # print(url)

        # print(player)
        for i in range(retries):
            print(f"Attempt {i}")
            try:
                driver.get(url)
                html = driver.page_source
                games = get_player_games(html, player, year)
                master_list.extend(games)
                # print("* masterlist"*10)
                # print(master_list)
                # print("*"*10)

                # to_csv(games, year, p_name)
                from datetime import datetime
                now = datetime.today().strftime('%Y-%m-%d')
                pd.DataFrame(master_list).to_csv(f"./data/games_{now}.csv", index=False)

                break
            except Exception:
                print(sys.exc_info()[0])
                print('get_data(): error')
                print(url)
                driver.close()
                driver.quit()
                driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
                continue



                #continue
            finally:
                time.sleep(sleep * i)

    return driver

def get_player_games(html, player, year):
    print('searching for games for ', player)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table", {'id': 'pgl_basic'}).find('tbody')
    if table == None:
        return False

    rows = table.find_all('tr')
    games = []
    for row in rows:
        game = {}
        game['player'] = player
        for td in row.find_all('td'):
            game[td['data-stat']] = td.text

        # print(game)
        game = game_util.convert_game(game)

        # print(game)
        if game != None:
            # add_to_database(game)
            games.append(game)
            # return True
        # return False
    return games

    # pd.DataFrame(games).to_csv(f'./data/nba_data/{player}_{year}.csv')
    # print(game)

