
if __name__ == '__main__':
    import requests
    from time import sleep

    url = 'https://datsorange.devteam.games/buyStock'

    while True:
        response = requests.get(url, headers={'token': '64f8a82b0ee5c64f8a82b0ee60'})
        data = []
        dates = set()
        #print(response.json())
        arr = []
        for i in response.json():
            if i['bids']:
                for bid in i['bids']:
                    arr.append([bid['price'], bid['quantity'], bid['quantity'], i['ticker']])
        arr.sort()
        for i in arr:
            print(i)
        print()
        print(arr)

        sleep(30)