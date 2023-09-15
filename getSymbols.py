import requests
import json

def getSymbols():
    url = 'https://datsorange.devteam.games/getSymbols'
    response = requests.get(url, headers={'token': '64f8a82b0ee5c64f8a82b0ee60'})
    pretty_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
    print(pretty_json)

if __name__=="__main__":
    getSymbols()