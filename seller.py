import requests
import json

def getSymbols():
    url = 'https://datsorange.devteam.games/LimitPriceSell'
    response = requests.get(url, headers={'token': '64f8a82b0ee5c64f8a82b0ee60'})
    data = []
    dates = set()
    cnt = 20
    # print(response.json())
    arr = []
    for i in response.json():
        if i['bids']:
            for bid in i['bids']:
                if bid['price'] / bid['quantity'] <= 0.05:
                    arr.append([bid['price'], bid['quantity'], i['ticker']])
                    res = requests.post('https://datsorange.devteam.games/LimitPriceSell', headers={
                        'token': '64f8a82b0ee5c64f8a82b0ee60'},
                                        params={
                                            "symbolId": 16,
                                            "price": 1,
                                            "quantity": max(0, cnt)
                                        }).json()
                    cnt = 0
                    print(res)
                    break
        if not cnt:
            break
            # print(res['bidId'], res['price'], res['message'])
    arr.sort()
    for i in arr:
        print(i)
    print()
    print(arr)

    sleep(30)

if __name__=="__main__":
    getSymbols()