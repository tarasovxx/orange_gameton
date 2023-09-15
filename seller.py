import requests
import json
import time
while True:
    res = requests.post('https://datsorange.devteam.games/LimitPriceSell', headers={
        'token': '64f8a82b0ee5c64f8a82b0ee60'},
                        json={
                            "symbolId": 16,
                            "price": 15000,
                            "quantity": 1
                        }).json()
    print(res)
    time.sleep(20)
