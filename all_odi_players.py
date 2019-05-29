import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

fake_user = UserAgent()
responce = requests.get('https://en.wikipedia.org/wiki/List_of_One_Day_International_cricketers', headers = {'fake-user' : fake_user.chrome})

soup = BeautifulSoup(responce.text, 'lxml')

teams = [team.text for team in soup.find_all('span', class_="mw-headline")]

players_data =[i for i in soup.find_all('small')]

teams_and_players = {}
for index,players in enumerate(players_data):
    teams_and_players[teams[index]] = []
    for player in players.find_all('a'):
        teams_and_players[teams[index]].append(player.text)


for team_name,players in teams_and_players.items():
    print(team_name + ' ' ,players )