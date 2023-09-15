import requests
import json

from time import sleep

def getInfo():
    url = 'https://datsorange.devteam.games/news/LatestNews5Minutes'
    url = 'https://datsorange.devteam.games/info'

    while True:
        # response = requests.get(url, headers={'token': '64f8a82b0ee5c64f8a82b0ee60'})
        # 6501a0cc7ec5a6501a0cc7ec5c - адмирал
        # response = requests.get(url, headers={'token': '64f60ea55e27164f60ea55e273'}) # тюбики
        # response = requests.get(url, headers={'token': '64fb4ccc14fd064fb4ccc14fd3'}) # Райан Гослинг в фильме Драйв
        response = requests.get(url, headers={'token': '64f433d6143b064f433d6143b3'}) # Давно кодеры
        # token = "64f433d6143b064f433d6143b3"
        json_data = response.json()
        formatted_json = json.dumps(json_data, indent=4)
        print(formatted_json)
        sleep(30)

if __name__=="__main__":
    getInfo()