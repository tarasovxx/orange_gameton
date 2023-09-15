
if __name__ == '__main__':
    import requests
    from time import sleep

    url = 'https://datsorange.devteam.games/news/LatestNews5Minutes'

    while True:
        response = requests.get(url)
        data = []
        dates = set()

        for i in response.json():
            if i['date'] not in dates:
                print(i)
                dates.add(i['date'])
                data.append([i['rate'], i['date'], i['text'], i['companiesAffected']])
        sleep(30)


