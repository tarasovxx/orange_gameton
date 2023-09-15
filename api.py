import requests


def make_request(url: str, token: str, method='GET', **kwargs):
    return requests.request(method=method, url=url, headers={
        'token': token,
        'Content-Type': 'application/json'
    }, **kwargs)


class Bid:
    @staticmethod
    def remove_bid(token: str, bid_id: int) -> bool:
        """
        Отменяет заявку
        """
        return make_request(
            url='https://datsorange.devteam.games/RemoveBid',
            token=token,
            method='POST',
            json=dict(bidId=bid_id)
        ).ok

    @staticmethod
    def limit_price_sell(token: str, symbol_id: int, price: int, quantity: int) -> bool:
        """
        Размещает заявку на продажу по цене не менее установленной
        """
        return make_request(
            url='https://datsorange.devteam.games/LimitPriceSell',
            token=token,
            method='POST',
            json=dict(symbolId=symbol_id, price=price, quantity=quantity)
        ).ok

    @staticmethod
    def limit_price_buy(token: str, symbol_id: int, price: int, quantity: int) -> bool:
        """
        Размещает заявку на покупку по цене не более установленной
        """
        return make_request(
            url='https://datsorange.devteam.games/LimitPriceBuy',
            token=token,
            method='POST',
            json=dict(symbolId=symbol_id, price=price, quantity=quantity)
        ).ok

    @staticmethod
    def best_price_sell(token: str, symbol_id: int, quantity: int) -> bool:
        """
        Размещает заявку на продажу по 'лучшей цене'
        """
        return make_request(
            url='https://datsorange.devteam.games/BestPriceSell',
            token=token,
            method='POST',
            json=dict(symbolId=symbol_id, quantity=quantity)
        ).ok

    @staticmethod
    def best_price_buy(token: str, symbol_id: int, quantity: int) -> bool:
        """
        Размещает заявку на покупку по 'лучшей цене'
        """
        return make_request(
            url='https://datsorange.devteam.games/BestPriceBuy',
            token=token,
            method='POST',
            json=dict(symbolId=symbol_id, quantity=quantity)
        ).ok


class Stock:
    @staticmethod
    def sell_stock(token: str) -> list[dict]:
        """
        Заявки на продажу.
        Возвращает количество активных заявок и их цену
        """
        response = make_request(
            url='https://datsorange.devteam.games/sellStock',
            token=token
        )
        return response.json()

    @staticmethod
    def get_symbols(token: str) -> list[dict]:
        """
        Список всех активов.
        Возвращает список всех возможных активов
        """
        response = make_request(
            url='https://datsorange.devteam.games/getSymbols',
            token=token
        )
        return response.json()

    @staticmethod
    def buy_stock(token: str) -> list[dict]:
        """
        Список всех активов.
        Возвращает список всех возможных активов
        """
        response = make_request(
            url='https://datsorange.devteam.games/buyStock',
            token=token
        )
        return response.json()


class News:
    @staticmethod
    def latest_news(token: str) -> list[dict]:
        """
        Возвращает новости за последние 5 минут
        """
        return make_request(
            url='https://datsorange.devteam.games/news/LatestNews5Minutes',
            token=token
        ).json()


class Info:
    @staticmethod
    def info(token: str) -> list[dict]:
        """
        Информация о счете
        """
        return make_request(
            url='https://datsorange.devteam.games/info',
            token=token
        ).json()
