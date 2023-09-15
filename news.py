# TODO:
# Слово диведенды - сигнал на покупку
# More Rate-> More buy
#
if __name__ == '__main__':
    import requests
    from time import sleep

    url_5min = 'https://datsorange.devteam.games/news/LatestNews5Minutes'
    url_news = 'https://datsorange.devteam.games/news/LatestNews'
    url_news1 = 'https://datsorange.devteam.games/news/LatestNews1Minute'

    while True:
        response = requests.get(url_5min)
        data = []
        dates = set()

        for i in response.json():
            if i['date'] not in dates:
                print(i)
                dates.add(i['date'])
                data.append([i['rate'], i['date'], i['text'], i['companiesAffected']])
        sleep(30)
