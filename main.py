import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

pd.set_option('display.max_columns', None)

from game_util import convert_game
from player_util import get_player_list
from web_util import get_data

def to_csv(games, year, player):
    import os
    import pandas as pd
    print('saving')
    try:
        directory = f'./data/{year}/'
        if not os.path.exists(directory):
            os.makedirs(directory)

        games = pd.DataFrame(games)
        games.to_csv(directory+ f'{player}.csv', index=False)
        return True
    except:
        print('error:to_csv()')
        return False







# connection = sqlite3.connect('./databases/nba_db.db')

# sql = """

#                     create table if not exists games(
#                     game_id text PRIMARY KEY,
#                     player text,
#                     game_date text,
#                     team text,
#                     opp text,
#                     is_home boolean,
#                     mp integar,
#                     fg integar,
#                     fga integar,
#                     fg3 integar,
#                     fg3a integar,
#                     ft integar,
#                     fta integar,
#                     orb integar,
#                     drb integar,
#                     ast integar,
#                     stl integar,
#                     blk integar,
#                     pts integar
#                     )
#                 """

# connection.execute(sql)
# connection.commit()


if __name__ == '__main__':
    failed_names = []
    curr_year = 2023
    for year in range(2023, curr_year+1):
        players = get_player_list(year)
        driver = get_data(players, year)

    driver.close()
    driver.quit()

    # with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
    #     for year in range(2023, 2024):
    #         players = get_player_list(year)
    #         get_data(players, driver, year)

    # driver.close()
    # driver.quit()