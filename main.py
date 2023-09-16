"""
1. Получаем все заявки на покупку
2. Получаем все акции мамонта
3. Получаем все акции мамонта, которых нет на рынке
4. ЮЗЕР: Покупаем акцию X за 1 апельсин
5. МАМОНТ: Выставляем нерыночную акцию X за 1 апельсин
6. МАМОНТ: Покупаем акцию X за Y апельсинов
7. ЮЗЕР: Выставляем акцию X за Y апельсинов
"""

from api import Stock, Info, Bid
from config import TRIO_TOKEN, fake_tokens
from time import sleep


def scam(user_token: str, mammoth_token: str):
    valid_key_id = []
    while (len(valid_key_id) == 0):
        # 1. Получаем все заявки на покупку
        buy_stocks: list[dict] = Stock.buy_stock(user_token)
        # print(buy_stocks)
        buy_stocks = sorted(buy_stocks, key=lambda x: len(x['bids']), reverse=True)
        print(buy_stocks[:10])
        break
        # example response: {'id': 1598, 'ticker': 'Oranges/CyberOcean Robotics', 'bids': []}
        # 2. Получаем все акции мамонта с ненулевым quantity
        mammoth: dict = Info.info(mammoth_token)
        stocks_available_at_mammoth = {}
        for stocks in mammoth['assets']:
            if stocks['quantity'] > 0:
                stocks_available_at_mammoth[stocks['id']] = stocks
        # example response: {'id': 1, 'name': 'Oranges', 'quantity': 2089}
        # mammoth_assets: list[dict] = list(filter(
        #     lambda x: x['quantity'] != 0,
        #     mammoth['assets']
        # ))
        # 3. Получаем все акции мамонта, которых нет на рынке

            # all_stock_mammoth_valide :::: {124: {'id': 124, 'name': 'ExpertCompanion Inc.', 'quantity': 3}}

        stock_is_not_on_the_market = {}
        for cur in buy_stocks:
            if len(cur['bids']) == 0:
                stock_is_not_on_the_market[cur['id']] = cur
        all_stock_mammoth_valide = {}
        for id, other in stocks_available_at_mammoth.items():
            if (id in stock_is_not_on_the_market.keys()):
                all_stock_mammoth_valide[id] = other
        for key_id, other in all_stock_mammoth_valide.items():
            valid_key_id.append(key_id)
        print("Sleep")
        sleep(2)


    print(valid_key_id)

    # cur_balance_mammoth = Info.getCurBalance(mammoth_token)
    # cur_balance_user = Info.getCurBalance(user_token)
    # print(cur_balance_mammoth)
    # print(cur_balance_user)
    # delta_price = 100
    # # 4. ЮЗЕР: Покупаем нерыночную акцию X за 1 апельсин
    # checker1 = Bid.limit_price_buy(user_token, valid_key_id[0], 1, 1)
    # print(checker1)
    # # # 5. МАМОНТ: Выставляем нерыночную акцию X за 1 апельсин
    # checker2 = Bid.limit_price_sell(mammoth_token, valid_key_id[0], 1, 1)
    # print(checker2)
    # # # 6. МАМОНТ: Покупаем акцию X за Y апельсинов 325 436 157
    # checker3 = Bid.limit_price_buy(mammoth_token, valid_key_id[0], delta_price, 1)
    # print(checker3)
    # # 7. ЮЗЕР: Выставляем акцию X за Y апельсинов
    # checker4 = Bid.limit_price_sell(user_token, valid_key_id[0], delta_price, 1)
    # print(checker4)
    #
    # cur_balance_mammoth = Info.getCurBalance(mammoth_token)
    # cur_balance_user = Info.getCurBalance(user_token)
    # print("------------------------------------")
    # print(cur_balance_mammoth)
    # print(cur_balance_user)
    # infrom_acc = Info.info(TRIO_TOKEN)
    # print(infrom_acc['frozenAssets'])


if __name__=="__main__":
    scam(TRIO_TOKEN, fake_tokens[1]) # 44688 -> 43595