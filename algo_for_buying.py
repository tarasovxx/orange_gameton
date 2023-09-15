import json

if __name__ == '__main__':
    import requests
    from time import sleep


    def buy_stock(stock_name, amount):
        url = 'https://datsorange.devteam.games/buyStock'
        response = requests.get(url, headers={'token': '64f8a82b0ee5c64f8a82b0ee60'})
        cnt = amount * 4
        arr = []
        for i in response.json():
            if i['bids']:
                for bid in i['bids']:
                    if bid['price'] / bid['quantity'] <= 0.05:
                        arr.append([bid['price'], bid['quantity'], i['ticker']])
                        res = requests.post('https://datsorange.devteam.games/LimitPriceBuy', headers={
                            'token': '64f8a82b0ee5c64f8a82b0ee60'},
                                            params={
                                                "symbolId": 16,
                                                "price": 1,
                                                "quantity": max(0, cnt)
                                            }).json()
                        cnt = 0
                        print(res)

        print(f"Куплено {amount} акций {stock_name}")


    def sell_stock(stock_name):
        # Здесь должен быть код для продажи акций stock_name в количестве amount
        # Например, запрос к бирже или симулятору торговли
        print(f"Продано {amount} акций {stock_name}")

    url = 'https://datsorange.devteam.games/news/LatestNews5Minutes'
    url_info = 'https://datsorange.devteam.games/info'

    while True:
        response = requests.get(url)
        response_info = requests.get(url, headers={'token': '64f8a82b0ee5c64f8a82b0ee60'})
        data = []
        dates = set()
        parsed_data = json.loads(response_info)
        names_set = {asset["name"] for asset in parsed_data["assets"]}

        for i in response.json():
            if i['date'] not in dates:
                print(i)
                dates.add(i['date'])
                data.append([i['rate'], i['date'], i['text'], i['companiesAffected']])

                rate = i['rate']
                stock_name = i['companiesAffected'] # здесь нужно проверить, есть ли у нас акции данной комании
                for j in stock_name:
                    if j in names_set:
                        if (rate > 0):
                            buy_stock(j, rate) # если пришли плохие вести дропаем всё, иначе докупаем
                        else:
                            sell_stock(j)

        sleep(30)


