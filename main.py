import requests
import json

from time import sleep

def getInfo():
    url = 'https://datsorange.devteam.games/news/LatestNews5Minutes'
    url = 'https://datsorange.devteam.games/info'

    while True:
        response = requests.get(url, headers={'token': '64f8a82b0ee5c64f8a82b0ee60'})
        json_data = response.json()
        formatted_json = json.dumps(json_data, indent=4)
        print(formatted_json)
        sleep(30)

if __name__=="__main__":
    getInfo()