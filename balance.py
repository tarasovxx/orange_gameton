if __name__ == '__main__':
    import requests
    from time import sleep

    url = 'https://datsorange.devteam.games/info'

    while True:
        response = requests.get(url, headers={'token': '64f8a82b0ee5c64f8a82b0ee60'})
        print(response.text)
        data = []
        dates = set()

        sleep(30)
